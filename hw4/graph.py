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
from typing import Any

class Vertex:
    """
    Class to represent a vertex in a directed, weighted multigraph
    """

    __name: str
    __attributes: dict[str, Any]
    __out_edges: dict[str, set["Edge"]]
    
    def __init__(self, name: str):
        """
        Constructor

        Parameters:
            name [str]: identifier for the vertex
        """
        self.__name = name
        self.__attributes = {}
        self.__out_edges = {}
    
    @property
    def name(self) -> str:
        """
        Get the name of a vertex

        Parameters: none beyond self

        Returns [str]: the name
        """
        return self.__name
    
    def set_attribute(self, key: str, val: Any) -> None:
        """
        Set the value of a given attribute

        Parameters:
            key [str]: the key under which to store the value
            value [Any]: the value to store for the key

        Returns: nothing
        """
        self.__attributes[key] = val
    
    def get_attribute(self, key: str) -> Any:
        """
        Retrieve the value of a given attribute
        
        Parameters:
            key [str]: the key of the desired attribute

        Returns [Any]: the value associated with the key, or None if the key
            does not exist
        """
        return self.__attributes.get(key)
    
    def add_out_edge(self, edge: "Edge") -> None:
        """
        Add an outgoing edge to the vertex

        Parameters:
            edge [Edge]: the edge to add

        Returns: nothing
        
        Raises:
            ValueError: if the edge has a different origin
        """
        if edge.origin is not self:
            raise ValueError("adding edge out of vertex with different origin")
        dest_name = edge.destination.name
        
        if dest_name not in self.__out_edges:
            self.__out_edges[dest_name] = set()
        
        self.__out_edges[dest_name].add(edge)
    
    @property
    def out_neighbors(self) -> set[str]:
        """
        Finds the set of vertex identifiers for vertices to which this vertex
            has outgoing edges

        Parameters: none beyond self

        Returns [set[str]]: the set of neighbors' vertex identifiers
        """
        return set(self.__out_edges.keys())
    
    def get_edges_to(self, destination: str) -> set["Edge"]:
        """
        Find the edges from this vertex to another specified vertex

        Parameters:
            destination [str]: the destination vertex's identifier

        Returns [set[Edge]]: the set of edges from this vertex to the
            destination
        """
        return self.__out_edges.get(destination, set())
    
    def __str__(self) -> str:
        """
        Generate a string representation of this vertex

        Parameters: none beyond self

        Returns [str]: a string representation
        """
        combined_edges: set[Edge] = set()
        for es in self.__out_edges.values():
            combined_edges = combined_edges.union(es)
        edge_strs = ",\n\t".join([str(e) for e in combined_edges])
        return f"Vertex({self.__name},\n\t[{edge_strs}])"

class Edge:
    """
    Class to represent an edge in a directed, weighted multigraph
    """

    __origin: Vertex
    __destination: Vertex
    __weight: float
    __attributes: dict[str, Any]
    
    def __init__(self, origin: Vertex, destination: Vertex, weight: float):
        """
        Constructor

        Parameters:
            origin [Vertex]: origin vertex of the edge
            destination [Vertex]: destination vertex of the edge
            weight [float]: weight of the edge
        """
        self.__origin = origin
        self.__destination = destination
        self.__weight = weight
        self.__attributes = {}
        
    @property
    def origin(self) -> Vertex:
        """
        Get the origin of the edge

        Parameters: none beyond self

        Returns [Vertex]: the origin vertex
        """
        return self.__origin
    
    @property
    def destination(self) -> Vertex:
        """
        Get the destination vertex of the edge

        Parameters: none beyond self

        Returns [Vertex]: the destination vertex
        """
        return self.__destination
    
    @property
    def weight(self) -> float:
        """
        Get the weight of the edge

        Parameters: none beyond self

        Returns [float]: the weight
        """
        return self.__weight
    
    def set_attribute(self, key: str, val: Any) -> None:
        """
        Set the value of a given attribute

        Parameters:
            key [str]: the key under which to store the value
            value [Any]: the value to store for the key

        Returns: nothing
        """
        self.__attributes[key] = val
    
    def get_attribute(self, key: str) -> Any:
        """
        Retrieve the value of a given attribute
        
        Parameters:
            key [str]: the key of the desired attribute

        Returns [Any]: the value associated with the key, or None if the key
            does not exist
        """
        return self.__attributes.get(key)

    def __str__(self) -> str:
        """
        Generate a string representation of this edge

        Parameters: none beyond self

        Returns [str]: a string representation
        """
        return f"Edge({self.__origin.name} --{self.__weight}--> " + \
               f"{self.__destination.name} ({self.__attributes['Flight Number']}))"
    

class DirectedMultigraph:
    """
    Class to represent a directed, weighted multigraph
    """

    __vertices: dict[str, Vertex]
    
    def __init__(self) -> None:
        """
        Constructor

        Parameters: none beyond self
        """
        self.__vertices = {}
    
    def add_vertex(self, vertex: Vertex) -> None:
        """
        Add a vertex to the graph

        Parameters:
            vertex [Vertex]: the new vertex

        Returns: nothing
        
        Raises:
            ValueError: if a vertex with that identifier already exists
        """
        vertex_name = vertex.name
        if vertex_name in self.__vertices:
            raise ValueError("a vertex with that name is already in the graph")
        
        self.__vertices[vertex_name] = vertex
    
    def get_vertex(self, name: str) -> Vertex:
        """
        Get the vertex with the given identifier

        Parameters:
            name [str]: the identifier of the desired vertex

        Returns [Vertex]: the corresponding Vertex object
        
        Raises:
            ValueError: if there is no such vertex
        """
        if name not in self.__vertices:
            raise ValueError("no such vertex")
        return self.__vertices[name]
        

    def __str__(self) -> str:
        """
        Generate a string representation of the graph

        Parameters: none beyond self

        Returns [str]: a string representation
        """
        return "Graph:\n" + "\n".join([str(v) for v in
            self.__vertices.values()])
