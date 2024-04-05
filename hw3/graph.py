"""
CMSC 14200, Spring 2024
Homework #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
from image import Image, Color, Loc

class ImageGraph:
    """
    Class for a graph over an image where adjacent pixels are neighbors
    """

    def __init__(self, image: Image):
        """
        Constructor

        Parameters:
            image [Image]: the image over which to build the graph
        """
        ### TODO
        raise NotImplementedError()
    
    def neighbors(self, location: Loc) -> set[Loc]:
        """
        Determines the pixels adjacent to a given pixel in the graph, where
            adjacency is defined by being immediately above, below, to the
            left, or to the right

        Parameters:
            location [Loc]: the pixel whose neighbors to find

        Returns [set[Loc]]: the set of neighbors
        """
        ### TODO
        raise NotImplementedError()
    
    def find_outline(self, start: Loc) -> set[Loc]:
        """
        Determines the region of contiguous pixels surrounding the given
            starting pixel with the same color, then returns the set of pixels
            on the border between this region and other-colored regions or the
            edge of the image. Contiguity is defined by being directly above,
            below, to the left, or to the right.

        Parameters:
            start [Loc]: a pixel in the region to outline

        Returns [set[Loc]]: the outline of the region
        """
        ### TODO
        raise NotImplementedError()
    
