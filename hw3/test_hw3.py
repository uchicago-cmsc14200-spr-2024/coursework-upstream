import pytest

from image import Image, Loc, Color
from graph import ImageGraph

@pytest.mark.parametrize("filename, width, height, pixels",
    [["grid.ppm", 320, 192,
        [((0, 0), (0, 0, 255)),
         ((319, 0), (0, 0, 255)),
         ((0, 191), (0, 0, 255)),
         ((319, 191), (0, 0, 255)),
         ((7, 13), (0, 0, 255)),
         ((64, 23), (255, 255, 0)),
         ((128, 64), (255, 255, 0)),
         ((130, 135), (0, 0, 255))]],
     ["shapes.ppm", 800, 300,
        [((10, 20), (255, 255, 0)),
         ((100, 150), (255, 0, 0)),
         ((60, 55), (128, 128, 128)),
         ((375, 230), (0, 255, 0)),
         ((330, 60), (128, 128, 128)),
         ((720, 84), (0, 0, 255))]]])
def test_task1_image_load(filename: str, width: int, height: int,
                          pixels: list[tuple[Loc, Color]]) -> None:
    img = Image(filename)
    
    assert img.width == width, "incorrect image width"
    assert img.height == height, "incorrect image height"
    
    for loc, color in pixels:
        x, y = loc
        assert img.pixels[y][x] == color, "incorrect image pixel"


@pytest.mark.parametrize("center, expected",
    [[(0, 0), {(0, 1), (1, 0)}],
     [(319, 0), {(318, 0), (319, 1)}],
     [(0, 191), {(1, 191), (0, 190)}],
     [(319, 191), {(319, 190), (318, 191)}],
     [(0, 10), {(0, 9), (0, 11), (1, 10)}],
     [(20, 0), {(19, 0), (21, 0), (20, 1)}],
     [(319, 30), {(319, 29), (319, 31), (318, 30)}],
     [(40, 191), {(39, 191), (41, 191), (40, 190)}],
     [(20, 40), {(20, 41), (21, 40), (20, 39), (19, 40)}]])
def test_task2_neighbors(center: Loc, expected: set[Loc]) -> None:
    img = Image("grid.ppm")
    igr = ImageGraph(img)
    
    actual = igr.neighbors(center)
    assert actual == expected, "neighbors are incorrect"


@pytest.mark.parametrize("filebase, start",
    [["grid", (155, 98)],
     ["grid", (156, 31)],
     ["grid", (163, 162)],
     ["grid", (214, 100)],
     ["grid", (214, 151)],
     ["grid", (227, 28)],
     ["grid", (28, 106)],
     ["grid", (280, 37)],
     ["grid", (281, 160)],
     ["grid", (298, 85)],
     ["grid", (32, 160)],
     ["grid", (42, 42)],
     ["grid", (83, 24)],
     ["grid", (87, 100)],
     ["grid", (92, 159)],
     ["shapes", (167, 151)],
     ["shapes", (232, 229)],
     ["shapes", (234, 68)],
     ["shapes", (320, 160)],
     ["shapes", (432, 211)],
     ["shapes", (461, 88)],
     ["shapes", (525, 219)],
     ["shapes", (64, 69)],
     ["shapes", (65, 230)],
     ["shapes", (686, 106)]])
def test_task2_find_outline(filebase: str, start: Loc) -> None:
    with open(f"tests/{filebase}-{start[0]}-{start[1]}.txt") as f:
        lines = f.readlines()
    lines2 = [line.strip().split(",") for line in lines]
    expected = set([(int(line[0]), int(line[1])) for line in lines2])
    
    img = Image(filebase + ".ppm")
    igr = ImageGraph(img)
    
    actual = igr.find_outline(start)
    assert actual == expected, "outline is incorrect"
    
