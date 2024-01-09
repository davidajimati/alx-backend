#!/usr/bin/env python3

"""
Write a function named index_range that takes two
integer arguments page and page_size.
"""


def index_range(page, page_size) -> tuple:
    '''
    This function returns the beginning and ending index of a page
    of an API response
    '''
    answer = []
    end_index = page * page_size
    start_index = end_index - page_size
    answer.insert(0, start_index)
    answer.insert(1, end_index)
    return tuple(answer)
