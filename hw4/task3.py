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
from graph import *

def itinerary(network: DirectedMultigraph, origin: str, destination: str,
              earliest: int, min_layover: int) -> list[Edge]:
    """
    Find a shortest path between two airports and return a list of feasible
        flights between them, starting with flights from the origin airport no
        earlier than a specified time, and requiring layovers be at least a
        given number of minutes.
    
    Parameters:
        network [DirectedMultigraph]: the airline flight network
        origin [str]: the starting airport
        destination [str]: the desired destination
        earliest [int]: the earliest viable departure from the origin, in
            24-hour time
        min_layover [int]: the minimum number of minutes for a feasible layover

    Returns [list[Edge]]: the sequence of flights to take, empty if no
        itinerary found
    """
    ### TODO
    raise NotImplementedError()
