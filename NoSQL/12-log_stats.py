#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


def main():
    """ provides some stats about Nginx logs stored in MongoDB """
    with MongoClient('mongodb://127.0.0.1:27017') as client:
        logs = client.logs.nginx

        print(f"{logs.count_documents({})} logs")
        print("Methods:")
        print(f"\tmethod GET: {logs.count_documents({'method': 'GET'})}")
        print(f"\tmethod POST: {logs.count_documents({'method': 'POST'})}")
        print(f"\tmethod PUT: {logs.count_documents({'method': 'PUT'})}")
        print(f"\tmethod PATCH: {logs.count_documents({'method': 'PATCH'})}")
        print(f"\tmethod DELETE: {logs.count_documents({'method': 'DELETE'})}")
        print(f"{logs.count_documents({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()
