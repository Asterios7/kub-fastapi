from pymongo import MongoClient
from pymongo.database import Database
import os

DB_CONN_STRING = os.environ.get("MONGODB_CONN_STRING")


def get_db_connection(db_name='kub-fastapi-db') -> Database:
    """
    Creates mongo_db_connection, here it connects to
    the database named 'local' (you can modify this)

    Parameters
    ----------
    db_name : str
        The database name to connect to

    Returns
    -------
    db : pymongo.database.Database
        Database object for querying collections

    """
    client = MongoClient(DB_CONN_STRING)
    db = client[db_name]
    print("Connected to --PRODUCTION-- database!")
    return db
