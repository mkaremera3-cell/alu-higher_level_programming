#!/usr/bin/python3
"""Module for class to JSON"""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of an object"""
    return obj.__dict__
