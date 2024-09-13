from generate_dummyf import *

csv_date = generate_csv(file_size=5000, 
                        column_description={"id": "int", "name" : "str", "flag": "boolean"},
                        save_file_path="/Users/rubinakarki/Projects/compare-db-table/db_config"
                        )
