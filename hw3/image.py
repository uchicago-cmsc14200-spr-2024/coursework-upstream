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

Loc = tuple[int, int]
Color = tuple[int, int, int]

class Image:
    """
    Class for a bitmap image
    """

    pixels: list[list[Color]]
    
    def __init__(self, filename: str):
        """
        Constructor

        Parameters:
            filename [str]: path to a PPM file
        """
        ### TODO
        raise NotImplementedError()
        
    @property
    def width(self) -> int:
        """
        Provide the width of the image

        Parameters: none beyond self

        Returns [int]: the width
        """
        ### TODO
        raise NotImplementedError()
    
    @property
    def height(self) -> int:
        """
        Provide the height of the image

        Parameters: none beyond self

        Returns [int]: the height
        """
        ### TODO
        raise NotImplementedError()
        
