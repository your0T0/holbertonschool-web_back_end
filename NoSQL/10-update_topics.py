#!/usr/bin/env python3
"""This module provides a function that updates school topics."""


def update_topics(mongo_collection, name, topics):
    """Update topics for all school documents matching the given name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
