from abc import abstractmethod, ABC
from copy import deepcopy
from typing import Any


class NDArray(ABC):
    """
    Abstract class for n-dimensional arrays
    """

    @property
    @abstractmethod
    def shape(self) -> int | tuple[int, int]:
        """
        Return the shape of the data, either an int (for 1d array)
        or pair of ints (for 2d array) in row, col order.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def data(self) -> list[int] | list[list[int]]:
        """
        Return the data (either a list or list of lists).
        """
        raise NotImplementedError

    @abstractmethod
    def flatten(self) -> "NDArray1":
        """
        Flatten the data (either 1- or 2-dimensional)
        into a 1-dimensional array.
        """
        raise NotImplementedError

    @abstractmethod
    def reshape(self, n: int, m: int) -> "NDArray2":
        """
        Reshape the data into an n x m array.

        Raises ValueError if the data does not have n * m elements,
        in which case the NDArray cannot be reshaped as such.
        """
        raise NotImplementedError

class NDArray1(NDArray):

    _data: list[int]
    _shape: int

    def __init__(self, data: list[int]):
        """
        Construct an NDArray1 from a list of int.
        """
        raise NotImplementedError

    def __add__(self, other: Any) -> "NDArray1":
        """
        Add either an int or another NDArray1.
        Produce a new array (functional style).

        Raises ValueError if other is an NDArray1 of different shape.
        """
        raise NotImplementedError

    def __gt__(self, other: Any) -> list[bool]:
        """
        Return a list of bools indicating greater than given int.
        """
        raise NotImplementedError

    def __contains__(self, other: Any) -> bool:
        """
        Test whether the given int is in the array.
        """
        raise NotImplementedError

    def __eq__(self, other: Any) -> bool:
        """
        Test whether other is an NDArray1 with the same shape and
        containing the same numbers.
        """
        raise NotImplementedError

    @property
    def shape(self) -> int:
        """
        see NDArray
        """
        raise NotImplementedError

    @property
    def data(self) -> list[int]:
        """
        see NDArray
        """
        raise NotImplementedError

    def flatten(self) -> "NDArray1":
        """
        see NDArray
        """
        raise NotImplementedError

    def reshape(self, n: int, m: int) -> "NDArray2":
        """
        see NDArray
        """
        raise NotImplementedError


class NDArray2(NDArray):

    _data: list[list[int]]
    _shape: tuple[int, int]

    def __init__(self, data: list[list[int]]):
        """
        Construct an NDArray2 from a list of lists of int.

        Raises ValueError if list of lists is jagged.
        """
        raise NotImplementedError

    def __add__(self, other: Any) -> "NDArray2":
        """
        Add either an int or another NDArray2.
        Produce a new array (functional style).

        Raises ValueError if other is an NDArray2 of different shape.
        """
        raise NotImplementedError

    def __gt__(self, other: Any) -> list[list[bool]]:
        """
        Return a list of lists of bools indicating greater than given int.
        """
        raise NotImplementedError

    def __contains__(self, other: Any) -> bool:
        """
        Test whether the given int is in the array.
        """
        raise NotImplementedError

    def __eq__(self, other: Any) -> bool:
        """
        Test whether other is an NDArray2 with the same shape and
        containing the same numbers.
        """
        raise NotImplementedError

    @property
    def shape(self) -> tuple[int, int]:
        """
        see NDArray
        """
        raise NotImplementedError

    @property
    def data(self) -> list[list[int]]:
        """
        see NDArray
        """
        raise NotImplementedError

    def flatten(self) -> "NDArray1":
        """
        see NDArray
        """
        raise NotImplementedError

    def reshape(self, n: int, m: int) -> "NDArray2":
        """
        see NDArray
        """
        raise NotImplementedError
