#!/usr/bin/env python3
"""
Script to list all databases in MongoDB.
"""

import pymongo


def list_databases():
    """List all databases in MongoDB."""
    try:
        # Connect to MongoDB server
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

        # List all databases
        databases = client.list_database_names()

        # Print the list of databases
        for db in databases:
            print(db)

    except pymongo.errors.PyMongoError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    list_databases()
