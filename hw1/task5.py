"""
CMSC 14200, Spring 2024
Homework #1, Task #5

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import math
from abc import ABC, abstractmethod
from task4 import Box


class OrientedBox(Box):
    """
    Class to represent a box (rectangular cuboid) that is facing with one of its
        sides against a plane and that has a density
    """

