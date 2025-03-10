import pandas as pd
import pymysql
import sqlalchemy
import re
from sqlalchemy import create_engine

def excel_to_mariadb(excel_file, db_user, db_password, db_host, db_name, port=3306):
    """
    Export all sheets in an Excel file to tables in a MariaDB database
    
    Args:
        excel_file (str): Path to the Excel file
        db_user (str): MariaDB username
        db_password (str): MariaDB password
        db_host (str): MariaDB host address
        db_name (str): Database name to use
        port (int): MariaDB port (default 3306)
    """
    # Create SQLAlchemy engine for MariaDB connection
    connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{port}/{db_name}"
    engine = create_engine(connection_string)
    
    # Read Excel file and get sheet names
    xl = pd.ExcelFile(excel_file)
    sheet_names = xl.sheet_names
    
    print(f"Found {len(sheet_names)} sheets in {excel_file}")
    
    # Process each sheet
    for sheet_name in sheet_names:
        # Read the sheet data
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        
        # Clean column names (replace spaces with underscores, remove special characters)
        df.columns = [re.sub(r'[^\w]', '_', col).lower() for col in df.columns]
        
        # Clean table name (replace spaces with underscores, remove special characters)
        table_name = re.sub(r'[^\w]', '_', sheet_name).lower()
        
        # Export dataframe to MariaDB
        try:
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Successfully created table '{table_name}' with {len(df)} rows")
        except Exception as e:
            print(f"Error creating table '{table_name}': {e}")
    
    print("Export completed!")

if __name__ == "__main__":
    # Example usage (replace with your actual values)
    excel_file = r"C:\Users\Aliska\Downloads\file_db_nuovo\eptic_database_10_03.xlsx"
    db_user = "root"
    db_password = "eptic"
    db_host = "localhost"  
    db_name = "eptic_v3"
    
    excel_to_mariadb(excel_file, db_user, db_password, db_host, db_name)