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
from typing import Optional
from graph import *

def direct_flight_exists(network: DirectedMultigraph, 
                         origin: str, destination: str) -> bool:
    """
    Determine whether or not there is a direct flight from one airport to
        another.

    Args:
        network: flight network
        origin: origin airport
        destination: destination airport

    Returns: True if there is a direct flight from origin to destination,
        False otherwise. 
    """
    ### TODO
    raise NotImplementedError()

def get_direct_flights(network: DirectedMultigraph, 
                       origin: str) -> set[Edge]:
    """
    Get all of the direct flights out of an aiport.

    Args:
        network: flight network
        origin: origin airport

    Returns: A set of direct flights from origin, or the empty set if origin is
        not an airport in the network. 
    """
    ### TODO
    raise NotImplementedError()

def most_popular_origin(network: DirectedMultigraph, 
                        airports: list[str]) -> set[str]:
    """
    Find the most popular origin airport(s) in a flight network.

    Args:
        network: flight network
        airports: list of airports in the network

    Returns: The most popular origin airport(s) (most outgoing flights) in the
        flight network. Returns a set of one if there is a single most popular, 
        or a set of multiples if there is a tie. 

        If no airport in airports list are in the network, this function should 
        return the empty set. 
    """
    ### TODO
    raise NotImplementedError()

def most_popular_destination(network: DirectedMultigraph, 
                             airports: list[str]) -> set[str]:
    """
    Find the most popular destination airport(s) in a flight network.

    Args:
        network: flight network
        airports: list of airports in the network

    Returns: The most popular destination airport(s) (most incoming flights) in the
        flight network. Returns a set of one if there is a single most popular, 
        or a set of multiples if there is a tie. 

        If no airport in airports list are in the network, this function should 
        return the empty set. 
    """
    ### TODO
    raise NotImplementedError()
