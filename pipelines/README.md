# Pipelines

Developer-side code for updating EPTIC.

# Prerequisites

A dump of SkEPTIC's MariaDB database.

All video files uploaded on SkEPTIC

# Workflow 

This is the workflow to convert SkEPTIC data into data suitable for indexing on NoSketch Engine.

## On your machine

1. Create a MariaDB instance locally and import the dump. Refer to MariaDB documentation: https://mariadb.com/kb/en/

2. Setup database credentials in a config.json file, e.g.:

```json
{
    "database": {
        "name": "eptic",
        "user": "root",
        "password": "eptic",
        "host": "localhost",
        "port": 3306
    }
}

3. Copy locally and run extract_tables_db.py to extract tables to current working directory. Pass config.json path as argument. E.g. python db_connect.py --config 'D:\eptic\config.json'. This creates a folder with database tables as Excel files.

## On DIT's server

1. Clone the repository.

2. Copy the Excel files from your PC to the server, into the folder eptic.v4/1. database_tables.

3. Copy all video files from your PC to the server, into the folder eptic.v4/video

3. Use pipelines/align_texts_bertalign.py to check alignments.xlsx and align the texts that are not yet aligned and output the new .xml files with all alignments to 2. bertalign_alignments (TO UPDATE)

4. Use pipelines/pyannote.py to diarize interpreters. Has to be done from scratch every time so will take some time (TO UPDATE). This will update the interpreters Excel file

5. Export from Excel to NoSketch Engine-compliant files for tagging using database_to_pretgd.py (TO UPDATE, change generated video urls amongs other things, make sure no missing things). This will create them in folder eptic.v4/3. pre_pos_files

6. Tag all pre_pos_files on Sketch Engine and copy them from your PC to the eptic.v4/4. pos_tagged_files folder. When creating them name them using this format: eptic3_LANGUAGE_MODE_DIRECTION.vert, e.g. eptic3_de_sp_tt.vert (because this is the name that we use to refer to them in the registry files)

7. If new subcorpora were added as part of this update, add new registry files in 5. NoSkE_files, i.e. if there are .vert files for which we don't have a registry file with the same name already. Latest registry files are in eptic.v4/5. NoSkE_files/registry

8. Copy vertical files, XML alignments and, if present, new registry files from current server to bellatrix server (NoSketch Engine server)

9. Refer to docs/indexing_howto.txt and note_eptic_alice_indexing_2024_01_19.txt for details about indexing corpora on NoSketch Engine

10. Update corpora info on website. Latest website files are in eptic.v4/website

11. Update SkEPTIC's database. Convert Excel files into SQL database using https://sqlizer.io/