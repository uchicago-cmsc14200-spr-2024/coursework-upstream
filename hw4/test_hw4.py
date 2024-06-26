import pytest

from graph import Vertex
from task1 import load_flights
from task2 import direct_flight_exists, get_direct_flights, \
                  most_popular_origin, most_popular_destination
from task3 import itinerary

airports_tiny1 = {'ORD', 'RDM', 'DEN'}
airports_tiny2 = {'ORD', 'RDM', 'ICT', 'DEN'}
airports_tiny3 = {'RDM', 'LAX', 'DEN'}
airports_small = {'GRR', 'LAX', 'RDM', 'DEN', 'ICT', 'ORD'}
airports_data  = {'GRR', 'LAX', 'RDM', 'DEN', 'ICT', 'ORD'}

def test_task1_load_flights_tiny1() -> None:

    graph = load_flights("data/tiny1.asc")
    assert graph is not None

    def get_vertex(airport: str) -> Vertex:
        try:
            return graph.get_vertex(airport)
        except ValueError:
            assert False, f"Missing airport: {airport}"

    den = get_vertex("DEN")
    ord = get_vertex("ORD")
    rdm = get_vertex("RDM")

    # DEN

    assert den.name == "DEN"
    assert den.out_neighbors == {"ORD", "RDM"}

    den_to_ord = den.get_edges_to("ORD")
    den_to_rdm = den.get_edges_to("RDM")

    error_msg = "Edge from DEN to ORD"
    assert len(den_to_ord) == 1                            , error_msg
    edge = list(den_to_ord)[0]
    assert edge.origin == den                              , error_msg
    assert edge.destination == ord                         , error_msg
    assert edge.weight == 888.54                           , error_msg
    assert edge.get_attribute("Flight Number") == "AA2780" , error_msg
    assert edge.get_attribute("Departure") == 1031         , error_msg
    assert edge.get_attribute("Arrival") == 1359           , error_msg

    error_msg = "Edge from DEN to RDM"
    assert len(den_to_rdm) == 1                            , error_msg
    edge = list(den_to_rdm)[0]
    assert edge.origin == den                              , error_msg
    assert edge.destination == rdm                         , error_msg
    assert edge.weight == 898.66                           , error_msg
    assert edge.get_attribute("Flight Number") == "UA5828" , error_msg
    assert edge.get_attribute("Departure") == 1910         , error_msg
    assert edge.get_attribute("Arrival") == 2109           , error_msg

    # ORD

    assert ord.name == "ORD"
    assert ord.out_neighbors == {"DEN"}

    ord_to_den = ord.get_edges_to("DEN")

    error_msg = "Edge from ORD to DEN"
    assert len(ord_to_den) == 1                            , error_msg
    edge = list(ord_to_den)[0]
    assert edge.origin == ord                              , error_msg
    assert edge.destination == den                         , error_msg
    assert edge.weight == 888.54                           , error_msg
    assert edge.get_attribute("Flight Number") == "AA2470" , error_msg
    assert edge.get_attribute("Departure") == 1350         , error_msg
    assert edge.get_attribute("Arrival") == 1531           , error_msg

    # RDM

    assert rdm.name == "RDM"
    assert rdm.out_neighbors == {"DEN"}

    rdm_to_den = rdm.get_edges_to("DEN")

    error_msg = "Edge from RDM to DEN"
    assert len(rdm_to_den) == 1                            , error_msg
    edge = list(rdm_to_den)[0]
    assert edge.origin == rdm                              , error_msg
    assert edge.destination == den                         , error_msg
    assert edge.weight == 898.66                           , error_msg
    assert edge.get_attribute("Flight Number") == "UA5781" , error_msg
    assert edge.get_attribute("Departure") == 1340         , error_msg
    assert edge.get_attribute("Arrival") == 1659           , error_msg

    # Non-edges

    assert len(ord.get_edges_to("ORD")) == 0 , "Edges from ORD to ORD"
    assert len(den.get_edges_to("DEN")) == 0 , "Edges from DEN to DEN"
    assert len(rdm.get_edges_to("RDM")) == 0 , "Edges from RDM to RDM"
    assert len(ord.get_edges_to("RDM")) == 0 , "Edges from ORD to RDM"
    assert len(rdm.get_edges_to("ORD")) == 0 , "Edges from RDM to ORD"

@pytest.mark.parametrize(
  "filename, expected",
  [(
    "data/tiny1.asc",
    {'ORD': (1, 0), 'RDM': (1, 0), 'DEN': (2, 1)}
   ),
   (
    "data/tiny2.asc",
    {'ORD': (2, 0), 'RDM': (1, 0), 'ICT': (2, 1), 'DEN': (3, 1)}
   ),
   (
    "data/tiny3.asc",
    {'RDM': (2, 0), 'LAX': (2, 0), 'DEN': (2, 0)}
   ),
   (
    "data/small.asc",
    {'GRR': (2, 1), 'LAX': (3, 2), 'RDM': (2, 0),
     'DEN': (5, 1), 'ICT': (2, 1), 'ORD': (4, 0)}
   ),
   (
    "data/data.asc",
    {'GRR': (2, 15), 'LAX': (3, 22), 'RDM': (2, 0),
     'DEN': (5, 15), 'ICT': (2, 8),  'ORD': (4, 0)}
   ),
  ]
)
def test_task1_load_flights( \
  filename: str,
  expected: dict[str, tuple[int, int]]
) -> None:
    """
    Given a solution, test-case data was generated by running:

    > g = load_flights(filename)
    > { airport : \
          (len(g.get_vertex(airport).out_neighbors),       \
           len(g.get_vertex(airport).get_edges_to("ORD"))) \
         for airport in g.___vertex_names___() }
    """

    graph = load_flights(filename)
    assert graph is not None

    for airport, (num_out_edges, num_edges_to_ord) in expected.items():
        try:
            v = graph.get_vertex(airport)
            assert num_out_edges == len(v.out_neighbors), \
                   f"Num edges from {airport}"
            assert num_edges_to_ord == len(v.get_edges_to("ORD")), \
                   f"Num edges from {airport} to ORD from"
        except ValueError:
            assert False, f"Missing airport: {airport}"

@pytest.mark.parametrize(
  "filename, expected",
  [("data/tiny1.asc", [False, False]),
   ("data/tiny2.asc", [False, True ]),
   ("data/tiny3.asc", [False, False]),
   ("data/small.asc", [True , True ]),
   ("data/data.asc",  [True , True ]),
  ]
)
def test_task2_direct_flight_exists(
  filename: str,
  expected: list[bool]
) -> None:
    graph = load_flights(filename)
    assert graph is not None

    ord_to_lax = expected[0]
    assert direct_flight_exists(graph, "ORD", "LAX") == ord_to_lax, "ORD to LAX"

    ord_to_ict = expected[1]
    assert direct_flight_exists(graph, "ORD", "ICT") == ord_to_ict, "ORD to ICT"

@pytest.mark.parametrize(
  "filename, expected",
  [("data/tiny1.asc",
    {'DEN': 2, 'ORD': 1, 'ICT': 0, 'RDM': 1, 'LAX': 0, 'GRR': 0}
   ),
   ("data/tiny2.asc",
    {'DEN': 3, 'ORD': 2, 'ICT': 2, 'RDM': 1, 'LAX': 0, 'GRR': 0}
   ),
   ("data/tiny3.asc",
    {'DEN': 3, 'ORD': 0, 'ICT': 0, 'RDM': 2, 'LAX': 3, 'GRR': 0}
   ),
   ("data/small.asc",
    {'DEN': 6, 'ORD': 6, 'ICT': 2, 'RDM': 2, 'LAX': 5, 'GRR': 2}
   ),
   ("data/data.asc",
    {'DEN': 45, 'ORD': 60, 'ICT': 13, 'RDM': 4, 'LAX': 44, 'GRR': 18}
   ),
  ]
)
def test_task2_get_direct_flights(
  filename: str,
  expected: dict[str, int]
) -> None:
    graph = load_flights(filename)
    assert graph is not None
    for airport in airports_data:
        n = len(get_direct_flights(graph, airport))
        m = expected[airport]
        assert n == m, f"Expected number of flights from {airport}"

@pytest.mark.parametrize( \
  "filename, airports, expected",
  [("data/tiny1.asc", airports_tiny1, {'DEN'}),
   ("data/tiny2.asc", airports_tiny2, {'DEN'}),
   ("data/tiny3.asc", airports_tiny3, {'DEN', 'LAX'}),
   ("data/small.asc", airports_small, {'DEN', 'ORD'}),
   ("data/data.asc",  airports_data , {'ORD'}),
  ]
)
def test_task2_most_popular_origin(
  filename: str,
  airports: set[str],
  expected: set[str]
) -> None:
    graph = load_flights(filename)
    assert graph is not None
    actual = most_popular_origin(graph, list(airports))
    assert actual == expected, f"Most popular origin in: {filename}"

@pytest.mark.parametrize( \
  "filename, airports, expected",
  [("data/tiny1.asc", airports_tiny1, {'DEN'}),
   ("data/tiny2.asc", airports_tiny2, {'DEN'}),
   ("data/tiny3.asc", airports_tiny3, {'DEN', 'LAX'}),
   ("data/small.asc", airports_small, {'DEN', 'LAX'}),
   ("data/data.asc",  airports_data , {'ORD'}),
  ]
)
def test_task2_most_popular_destination(
  filename: str,
  airports: set[str],
  expected: set[str]
) -> None:
    graph = load_flights(filename)
    assert graph is not None
    actual = most_popular_destination(graph, list(airports))
    assert actual == expected, f"Most popular destination in: {filename}"

@pytest.mark.parametrize("filename, origin, destination, earliest,"
                         "min_layover, expected",
    [["data/data.asc", "RDM", "LAX", 900, 45, ["UA5644"]],
     ["data/data.asc", "RDM", "LAX", 1600, 240, []],
     ["data/data.asc", "RDM", "GRR", 900, 45, []],
     ["data/data.asc", "RDM", "GRR", 1300, 45, ["UA5644", "UA660", "UA5727"]],
     ["data/data.asc", "RDM", "GRR", 1300, 240, []],
     ["data/data.asc", "RDM", "ICT", 900, 45, ["UA5781", "UA4775"]],
     ["data/data.asc", "RDM", "ICT", 900, 90, ["UA5781", "UA2300"]],
     ["data/data.asc", "RDM", "ICT", 900, 240, []],
     ["data/data.asc", "RDM", "ICT", 1300, 45, ["UA5644", "UA660", "AA3124"]],
     ["data/data.asc", "RDM", "DEN", 900, 45, ["UA5781"]],
     ["data/data.asc", "RDM", "DEN", 1300, 45, ["UA5644", "UA660", "UA675"]],
     ["data/data.asc", "RDM", "DEN", 1300, 240, []],
     ["data/data.asc", "RDM", "ORD", 900, 45, ["UA5781", "UA254"]],
     ["data/data.asc", "RDM", "ORD", 900, 90, ["UA5781", "UA1150"]],
     ["data/data.asc", "RDM", "ORD", 900, 240, []],
     ["data/data.asc", "RDM", "ORD", 1300, 45, ["UA5644", "UA660"]],
     ["data/data.asc", "LAX", "RDM", 900, 45, ["UA5508"]],
     ["data/data.asc", "LAX", "RDM", 1300, 240, []],
     ["data/data.asc", "LAX", "GRR", 900, 45, ["UA2049", "UA1510"]],
     ["data/data.asc", "LAX", "GRR", 900, 240, ["AA2776", "UA5727"]],
     ["data/data.asc", "LAX", "GRR", 1600, 240, ["UA660", "UA4261"]],
     ["data/data.asc", "LAX", "ICT", 900, 45, ["UA2049", "UA4775"]],
     ["data/data.asc", "LAX", "ICT", 900, 240, ["AA2776", "AA3124"]],
     ["data/data.asc", "LAX", "ICT", 1300, 45, ["DL2503", "UA2300"]],
     ["data/data.asc", "LAX", "ICT", 1300, 90, ["WN355", "UA2300"]],
     ["data/data.asc", "LAX", "ICT", 1300, 240, ["AA2776", "AA3124"]],
     ["data/data.asc", "LAX", "ICT", 1600, 240, ["UA660", "AA3124"]],
     ["data/data.asc", "LAX", "DEN", 900, 45, ["UA2049"]],
     ["data/data.asc", "LAX", "DEN", 900, 240, ["UA314"]],
     ["data/data.asc", "LAX", "DEN", 1300, 45, ["DL2503"]],
     ["data/data.asc", "LAX", "DEN", 1300, 90, ["WN355"]],
     ["data/data.asc", "LAX", "DEN", 1300, 240, ["UA750"]],
     ["data/data.asc", "LAX", "DEN", 1600, 240, ["WN1249"]],
     ["data/data.asc", "LAX", "ORD", 900, 45, ["AA2776"]],
     ["data/data.asc", "LAX", "ORD", 1600, 240, ["UA660"]],
     ["data/data.asc", "GRR", "RDM", 900, 45, ["WN1689", "UA5828"]],
     ["data/data.asc", "GRR", "RDM", 900, 240, []],
     ["data/data.asc", "GRR", "RDM", 1600, 45, ["UA4597", "UA5828"]],
     ["data/data.asc", "GRR", "RDM", 1600, 90, []],
     ["data/data.asc", "GRR", "LAX", 900, 45, ["WN1689", "WN1903"]],
     ["data/data.asc", "GRR", "LAX", 900, 240, ["WN1689", "WN2379"]],
     ["data/data.asc", "GRR", "LAX", 1300, 240, ["UA4597", "UA1409"]],
     ["data/data.asc", "GRR", "LAX", 1600, 45, ["UA4597", "DL2446"]],
     ["data/data.asc", "GRR", "LAX", 1600, 90, ["UA320", "AA1039"]],
     ["data/data.asc", "GRR", "LAX", 1600, 240, []],
     ["data/data.asc", "GRR", "ICT", 900, 45, ["UA5287", "AA3124"]],
     ["data/data.asc", "GRR", "ICT", 900, 90, ["AA3859", "AA3124"]],
     ["data/data.asc", "GRR", "ICT", 900, 240, ["AA3657", "AA3124"]],
     ["data/data.asc", "GRR", "ICT", 1300, 90, ["UA4061", "AA3124"]],
     ["data/data.asc", "GRR", "ICT", 1300, 240, ["AA3453", "AA3124"]],
     ["data/data.asc", "GRR", "ICT", 1600, 45, ["AA3453", "AA3124"]],
     ["data/data.asc", "GRR", "ICT", 1600, 90, ["UA320", "AA3124"]],
     ["data/data.asc", "GRR", "ICT", 1600, 240, []],
     ["data/data.asc", "GRR", "DEN", 900, 45, ["WN1689"]],
     ["data/data.asc", "GRR", "DEN", 1600, 45, ["UA4597"]],
     ["data/data.asc", "GRR", "DEN", 1600, 90, ["UA320", "AA1387"]],
     ["data/data.asc", "GRR", "DEN", 1600, 240, []],
     ["data/data.asc", "GRR", "ORD", 900, 45, ["UA5287"]]])
def test_task3_itinerary(filename: str, origin: str, destination: str,
                         earliest: int, min_layover: int,
                         expected: list[str]) -> None:
    dmg = load_flights(filename)
    assert dmg is not None, "could not load graph"

    actual = itinerary(dmg, origin, destination, earliest, min_layover)
    assert len(actual) == len(expected), "incorrect length of route"
    for act_f, exp_f in zip(actual, expected):
        assert act_f.get_attribute("Flight Number") == exp_f
