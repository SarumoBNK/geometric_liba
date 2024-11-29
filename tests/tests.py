import pytest
from circle import CircleDef
from square import SquareDef
from rectangle import RectangleDef
from triangle import TriangleDef

# Test cases for Circle
@pytest.mark.parametrize("radius, expected", [
    (5, 78.53981633974483),
    (10, 314.1592653589793),
    (23, 1661.9025137490005),
    (200_000, 125663706.14359172),
])
def test_circle_area(radius, expected):
    assert CircleDef.area(radius) == pytest.approx(expected)

@pytest.mark.parametrize("radius", ['5', -5])
def test_circle_invalid_area(radius):
    with pytest.raises((TypeError, ValueError)):
        CircleDef.area(radius)

@pytest.mark.parametrize("radius, expected", [
    (5, 31.41592653589793),
    (10, 62.83185307179586),
    (23, 144.51326206513048),
    (200_000, 1_256_637.0614359173),
])
def test_circle_perimeter(radius, expected):
    assert CircleDef.perimeter(radius) == pytest.approx(expected)

@pytest.mark.parametrize("radius", ['5', -5])
def test_circle_invalid_perimeter(radius):
    with pytest.raises((TypeError, ValueError)):
        CircleDef.perimeter(radius)

# Test cases for Square
@pytest.mark.parametrize("side, expected", [
    (7, 49),
    (10, 100),
    (23, 529),
    (200_000, 40_000_000_000),
])
def test_square_area(side, expected):
    assert SquareDef.area(side) == expected

@pytest.mark.parametrize("side, expected", [
    (5, 20),
    (10, 40),
    (23, 92),
    (200_000, 800_000),
])
def test_square_perimeter(side, expected):
    assert SquareDef.perimeter(side) == expected

@pytest.mark.parametrize("side", ['5', -5])
def test_square_invalid_input(side):
    with pytest.raises((TypeError, ValueError)):
        SquareDef.area(side)
    with pytest.raises((TypeError, ValueError)):
        SquareDef.perimeter(side)

# Test cases for Rectangle
@pytest.mark.parametrize("length, width, expected", [
    (7, 5, 35),
    (10, 10, 100),
    (23, 23, 529),
    (200_000, 200_000, 40_000_000_000),
])
def test_rectangle_area(length, width, expected):
    assert RectangleDef.area(length, width) == expected

@pytest.mark.parametrize("length, width, expected", [
    (5, 5, 20),
    (10, 10, 40),
    (23, 23, 92),
    (200_000, 200_000, 800_000),
])
def test_rectangle_perimeter(length, width, expected):
    assert RectangleDef.perimeter(length, width) == expected

@pytest.mark.parametrize("length, width", [(-5, 5), ('5', 5)])
def test_rectangle_invalid_input(length, width):
    with pytest.raises((TypeError, ValueError)):
        RectangleDef.area(length, width)
    with pytest.raises((TypeError, ValueError)):
        RectangleDef.perimeter(length, width)

# Test cases for Triangle
@pytest.mark.parametrize("base, height, expected", [
    (7, 5, 17.5),
    (10, 10, 50),
    (23, 23, 264.5),
    (200_000, 200_000, 20_000_000_000),
])
def test_triangle_area(base, height, expected):
    assert TriangleDef.area(base, height) == expected

@pytest.mark.parametrize("side1, side2, expected", [
    (5, 5, 15),
    (10, 10, 30),
    (23, 23, 69),
    (200_000, 200_000, 600_000),
])
def test_triangle_perimeter(side1, side2, expected):
    side3 = side1  # Assuming it's an equilateral triangle for simplicity
    assert TriangleDef.perimeter(side1, side2, side3) == expected

@pytest.mark.parametrize("base, height", [(-5, 5), ('5', 5)])
def test_triangle_invalid_input(base, height):
    with pytest.raises((TypeError, ValueError)):
        TriangleDef.area(base, height)
    with pytest.raises((TypeError, ValueError)):
        TriangleDef.perimeter(base, height, base)
