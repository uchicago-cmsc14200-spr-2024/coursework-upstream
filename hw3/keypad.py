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
import os
import sys


os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Keypad:
    """
    Class for a GUI-based keypad
    """

    def __init__(self, button_side: int = 32, spacer: int = 5,
                 font_size: int = 32, duration: int = 3):
        """
        Constructor

        Parameters:
            button_side [int]: side length of buttons
            spacer [int]: spacing between elements
            font_size [int]: font size for display
            duration [int]: number of frames to highlight button after click
        """
        ### TODO
        raise NotImplementedError()
    
    ### TODO: other methods

if __name__ == "__main__":
    Keypad()
