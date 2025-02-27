import json
import os
import pandas as pd
from sqlalchemy import create_engine, exc
import argparse

# Function to read database configuration from JSON file
def get_database_config_from_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        return data["database"]

# Function to connect to the database
def connect_to_db(config_data, db_name=None):
    database_name = db_name if db_name else config_data['name']
    connection_string = f"mariadb+mariadbconnector://{config_data['user']}:{config_data['password']}@{config_data['host']}:{config_data['port']}/{database_name}"
    engine = create_engine(connection_string)
    return engine

# Function to get all table names in the database
def get_table_names(connection):
    return pd.read_sql_query("SHOW TABLES;", connection)

# Function to perform a read operation 
def read_table_data(sql_query, connection):
    try:
        return pd.read_sql_query(sql_query, connection)
    except exc.SQLAlchemyError as e:
        print(f"An SQLAlchemy error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Main function to run the script
def main(config_path):
    config_data = get_database_config_from_json(config_path)
    print(f"Connecting to database: {config_data['name']}")
    engine = connect_to_db(config_data)
    output_folder = "database_tables"
    os.makedirs(output_folder, exist_ok=True)
    
    with engine.connect() as conn:
        table_names_df = get_table_names(conn)
        table_names = table_names_df[table_names_df.columns[0]].tolist()
        print(f"Tables in the database: {table_names}")
        
        for table in table_names:
            sql_query = f"SELECT * FROM {table}"
            df = read_table_data(sql_query, conn)
            
            if df is not None:
                output_path = os.path.join(output_folder, f"{table}.xlsx")
                df.to_excel(output_path, index=False)
                print(f"Data exported to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="Path to config JSON file")
    args = parser.parse_args()
    main(args.config)
