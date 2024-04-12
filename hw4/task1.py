"""
CMSC 14200, Spring 2024
Homework #4

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
import os
import csv
from typing import Optional
from graph import *

def load_flights(filename: str) -> Optional[DirectedMultigraph]:
    """
    Given a CSV file containing flight information, load that information
    into a DirectedMultigraph object.

    Args:
        filename: path to file

    Returns: The graph, or None if the file does not exist
    """
    if not os.path.exists(filename):
        return None

    flights = []
    with open(filename) as f:
        reader = csv.DictReader(f, delimiter="|")
        for row in reader:
            flights.append(row)

    ### YOUR CODE HERE ###
    raise NotImplementedError()
