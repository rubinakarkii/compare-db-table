# Compare DB Tables
## Project Description
This project provides tools to compare two database tables with the same column names. It identifies commonality, inserted rows, updated rows, and deleted rows using SQL and Python.

## Installation
1. Clone the Repository:

    ```
    git clone https://github.com/rubinakarkii/compare-db-table.git
    cd compare-db-table
    ```

2. Create a Virtual Environment:

    ```
    python -m venv venv
    source venv/bin/activate  
    ```

3. Install Dependencies:

    `pip install -r requirements.txt`

4. Set Up Environment Variables:

    Create a .env file in the root directory with the following content:

    ```
    DBNAME=your_db_name
    USER=your_db_user
    PASSWORD=your_db_password
    HOST=your_db_host
    PORT=your_db_port
    ```

## Usage
### Running dummy data generation script(OPTIONAL)
If you want to generate new dummy data, change value of save_file_path argument in generate_data.py to relative path of your db_config folder and run 
`python db_config/generate_data.py`

### Running populate script 
To create tables and populate them with dummy data
`python -m db_config.populate`

### Running the Main Script

*NOTES: Please alter(update, insert or delete) few rows/data in "target" table to actually see the differences between two tables*

To run the main script and interact with the database, execute:

`python main_asyncio.py` *FOR LARGE SIZED DATASETS*

`python main.py` *FOR SMALL TO MEDIUM SIZED DATASETS*

## Code Overview
`db_config/__init__.py`

Contains the SQLAlchemy engine, Base, and session configuration. This file loads environment variables, sets up the database connection, and defines the ORM base class.

`db_config/populate.py`

Script for populating or manipulating the database. It uses the database configuration from db_config/__init__.py.

`main_asyncio.py`
Main script for comparing the rows in two tables using asyncio

`main.py`

Main script for comparing the rows in two tables without using asyncio
