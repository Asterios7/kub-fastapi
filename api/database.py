from pymongo import MongoClient
import os

DB_CONN_STRING = os.environ["MONGODB_CONN_STRING"]

def get_db_connection():
    """
    Creates mongo_db_connection, here it connects to
    the database named 'local' (you can modify this)

    Returns
    -------
    db : pymongo.database.Database
        Database object for querying collections

    """
    client = MongoClient(DB_CONN_STRING)
    db = client['local']  # Define database e.g. 'local'
    print("Connected to --PRODUCTION-- database!")
    return db