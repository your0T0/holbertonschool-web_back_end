#!/usr/bin/env python3
"""This module provides a function that inserts a school document."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a MongoDB collection."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
