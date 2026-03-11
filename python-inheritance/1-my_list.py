#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """Inherits from list, adds print_sorted method"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
