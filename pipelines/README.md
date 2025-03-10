# Pipelines

Developer-side code for updating EPTIC.

# Prerequisites

A dump of SkEPTIC's MariaDB database.

All video files uploaded on SkEPTIC

# Workflow 

This is the workflow to convert SkEPTIC data into data suitable for indexing on NoSketch Engine.

## On your machine

1. Create a MariaDB instance locally. Refer to MariaDB documentation: https://mariadb.com/kb/en/

Then, connect to MariaDB using the command line client:

mysql -u username -p

Create the new database:

CREATE DATABASE skeptic2;

Use the source command to import the dump (note the path format):

USE skeptic2;
SOURCE C:/Users/Aliska/Desktop/eptic_2025-03-06.sql;

2. Setup database credentials in a config.json file, e.g. in this case:

```json
{
    "database": {
        "name": "skeptic2",
        "user": "root",
        "password": "eptic",
        "host": "localhost",
        "port": 3306
    }
}

3. Copy locally and run extract_data_from_db.py to extract tables to current working directory. Install any required dependencies if missing. Pass config.json path as argument. E.g. python extract_data_from_db.py --config 'D:\eptic\config.json'. This creates a folder with database tables as Excel files.

## On DIT's server

1. Clone the repository.

2. Copy the Excel files from your PC to the server, into the folder eptic.v6/1. database_tables.

3. Copy all video files from your PC to the server, into the folder eptic.v6/video

3. Use pipelines/align_texts_bertalign.py to check alignments.xlsx and align the texts that are not yet aligned and output the new .xml files with all alignments to your path, change line "xml_output_dir='/home/afedotova/EPTIC25/eptic.v5/2. bertalign_alignments'"

4. Use pipelines/diarize_and_genderize.py to update the interpreters. Has to be done from scratch every time so it takes some time. This will update the interpreters Excel file  ->> metti la colonna "native" lo stesso anche se vuota

5. Export from Excel to NoSketch Engine-compliant files for tagging using database_to_pretgd.py. This will create them in folder eptic.v4/3. pre_pos_files. If more languages are added to EPTIC, add them in the dictionary below "# Define full names for languages (add more if new languages are added to EPTIC)"   -----> FIX THE URLS, check empty lines

5.1 Use format_eptic_for_tagging.py to postprocess the .pretgd files before tagging on Sketch Engine (some words need to be adjusted so that the POS-tagger will recognize them correctly, such as truncated words)

6. Tag all pre_pos_files on Sketch Engine ("remember to check all boxes in Expert settings before compiling") and copy them from your PC to the eptic.v4/4. pos_tagged_files folder. When creating the filename, name them using this format: eptic3_LANGUAGE_MODE_DIRECTION.vert, e.g. eptic3_de_sp_tt.vert (because this is the name that we use to refer to them in the registry files). Remove <doc id= tag added by Sketch Engine

6.1 Use post_process_vert_files.py to add disfluency and pause tags to the POS-tagged .vert files. Adjust this code if new languages are added. Usage: python post_process_vert_files.py /home/afedotova/EPTIC25/eptic.v4/4.\ pos_tagged_files/fi_sp_tt.vert output_file.vert

7. If new subcorpora were added as part of this update, add new registry files in 5. NoSkE_files, i.e. if there are .vert files for which we don't have a registry file with the same name already. Latest registry files are in eptic.v4/5. NoSkE_files/registry

8. Copy vertical files, XML alignments and, if present, new registry files from current server to bellatrix.sslmit.unibo.it server (NoSketch Engine server)

9. Refer to docs/indexing_howto.txt and note_eptic_alice_indexing_2024_01_19.txt for details about indexing corpora on NoSketch Engine (CHECK THEM AGAIN)

10. Update corpora info on website. Latest website files are in eptic.v4/website

11. Update SkEPTIC's database. Convert Excel files into SQL database using https://sqlizer.io/

