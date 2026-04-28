#!/usr/bin/env python3
"""
This module provides a helper function for calculating pagination indexes.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return the start and end indexes for a given pagination page.

    Args:
        page: The current page number, starting from 1.
        page_size: The number of items on each page.

    Returns:
        A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index