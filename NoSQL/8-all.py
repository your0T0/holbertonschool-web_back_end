#!/usr/bin/env python3
"""This module provides a function that lists all MongoDB documents."""


def list_all(mongo_collection):
    """Return all documents in a MongoDB collection."""
    return list(mongo_collection.find())
