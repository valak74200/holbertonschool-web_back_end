#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def nginx_stats():
    """
    Display stats about nginx logs stored in MongoDB
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Get the logs database and nginx collection
    logs_collection = client.logs.nginx
    
    # Get total number of logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Print methods statistics
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    
    # Count status check logs
    status_check = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_stats()
