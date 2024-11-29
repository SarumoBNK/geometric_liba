import unittest
from circle import CircleDef
from square import SquareDef
from rectangle import RectangleDef
from triangle import TriangleDef

class TEST_CIRCLE_METHODS(unittest.TestCase):

    def test_square_mult(self):
        result = CircleDef.area(5) # 5*5*3.141592653589793
        self.assertEqual(result, 78.53981633974483)

        result = CircleDef.area(10) # 10*10*3.141592653589793
        self.assertEqual(result, 314.1592653589793)

        result = CircleDef.area(23) # 23*23*3.141592653589793
        self.assertEqual(result, 1661.9025137490005)

        result = CircleDef.area(200_000) # 200_000*200_000*3.141592653589793
        self.assertEqual(result, 125663706.14359172)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            CircleDef.area('5') # string input area

        with self.assertRaises(TypeError):
            CircleDef.perimeter('5') # string input perimeter

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            CircleDef.area(-5) # negative input area

        with self.assertRaises(ValueError):
            CircleDef.perimeter(-5) # negative input perimeter

    def test_zero_input(self):
        result = CircleDef.area(0) # zero input area
        self.assertEqual(result, 0)

        result = CircleDef.perimeter(0) # zero input perimeter
        self.assertEqual(result, 0)

    def test_float_input(self):
        result = CircleDef.area(5.5) # 5.5*5.5*3.141592653589793
        self.assertEqual(result, 95.03317777109125) #float input area

        result = CircleDef.perimeter(10.5) # 2*10.5*3.141592653589793
        self.assertEqual(result, 65.97344572538566) # float input perimeter

    def test_perimeter_mult(self):
        result = CircleDef.perimeter(5) # 2*5*3.141592653589793
        self.assertEqual(result, 31.41592653589793)

        result = CircleDef.perimeter(10) # 2*10*3.141592653589793
        self.assertEqual(result, 62.83185307179586)

        result = CircleDef.perimeter(23) # 2*23*3.141592653589793
        self.assertEqual(result, 144.51326206513048)

        result = CircleDef.perimeter(200_000) # 2*200_000*3.141592653589793
        self.assertEqual(result, 1_256_637.0614359173)

class TEST_SQUARE_METHODS(unittest.TestCase):

    def test_square_mult(self):
        result = SquareDef.area(7) # 7*7
        self.assertEqual(result, 49)

        result = SquareDef.area(10) # 10*10
        self.assertEqual(result, 100)

        result = SquareDef.area(23) # 23*23
        self.assertEqual(result, 529)

        result = SquareDef.area(200_000) # 200_000*200_000
        self.assertEqual(result, 40_000_000_000)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            SquareDef.area('5') # string input area

        with self.assertRaises(TypeError):
            SquareDef.perimeter('5') # string input perimeter

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            SquareDef.area(-5) # negative input area

        with self.assertRaises(ValueError):
            SquareDef.perimeter(-5) # negative input perimeter

    def test_zero_input(self):
        result = SquareDef.area(0) # zero input area
        self.assertEqual(result, 0)

        result = SquareDef.perimeter(0) # zero input perimeter
        self.assertEqual(result, 0)

    def test_float_input(self):
        result = SquareDef.area(5.5) # 5.5*5.5
        self.assertEqual(result, 30.25) #float input area

        result = SquareDef.perimeter(10.5) # 4*10.5
        self.assertEqual(result, 42) # float input perimeter

    def test_perimeter_mult(self):
        result = SquareDef.perimeter(5) # 4*5
        self.assertEqual(result, 20)
    
        result = SquareDef.perimeter(10) # 4*10
        self.assertEqual(result, 40)

        result = SquareDef.perimeter(23) # 4*23
        self.assertEqual(result, 92)

        result = SquareDef.perimeter(200_000) # 4*200_000
        self.assertEqual(result, 800_000) 

class TEST_RECTANGLE_METHODS(unittest.TestCase):

    def test_square_mult(self):
        result = RectangleDef.area(7, 5) # 7*5
        self.assertEqual(result, 35)

        result = RectangleDef.area(10, 10) # 10*10
        self.assertEqual(result, 100)

        result = RectangleDef.area(23, 23) # 23*23
        self.assertEqual(result, 529)

        result = RectangleDef.area(200_000, 200_000) # 200_000*200_000
        self.assertEqual(result, 40_000_000_000)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            RectangleDef.area('5', 5) # string input area

        with self.assertRaises(TypeError):
            RectangleDef.perimeter('5', 5) # string input perimeter

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            RectangleDef.area(-5, 5) # negative input area

        with self.assertRaises(ValueError):
            RectangleDef.perimeter(-5, 5) # negative input perimeter

    def test_zero_input(self):
        result = RectangleDef.area(0, 5) # zero input area
        self.assertEqual(result, 0)

        result = RectangleDef.perimeter(0, 5) # zero input perimeter
        self.assertEqual(result, 0)

    def test_float_input(self):
        result = RectangleDef.area(5.5, 5.5) # 5.5*5.5
        self.assertEqual(result, 30.25) #float input area

        result = RectangleDef.perimeter(10.5, 10.5) # 2*10.5 + 2*10.5
        self.assertEqual(result, 42) # float input perimeter

    def test_perimeter_mult(self):
        result = RectangleDef.perimeter(5, 5) # 2*5 + 2*5
        self.assertEqual(result, 20)
    
        result = RectangleDef.perimeter(10, 10) # 2*10 + 2*10
        self.assertEqual(result, 40)

        result = RectangleDef.perimeter(23, 23) # 2*23 + 2*23
        self.assertEqual(result, 92)

        result = RectangleDef.perimeter(200_000, 200_000) # 2*200_000 + 2*200_000
        self.assertEqual(result, 800_000)

class TEST_TRIANGLE_METHODS(unittest.TestCase):

    def test_square_mult(self):
        result = TriangleDef.area(7, 5) # 7*5/2
        self.assertEqual(result, 17.5)

        result = TriangleDef.area(10, 10) # 10*10/2
        self.assertEqual(result, 50)

        result = TriangleDef.area(23, 23) # 23*23/2
        self.assertEqual(result, 264.5)

        result = TriangleDef.area(200_000, 200_000) # 200_000*200_000/2
        self.assertEqual(result, 20_000_000_000)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            TriangleDef.area('5', 5) # string input area

        with self.assertRaises(TypeError):
            TriangleDef.perimeter('5', 5) # string input perimeter

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            TriangleDef.area(-5, 5) # negative input area

        with self.assertRaises(ValueError):
            TriangleDef.perimeter(-5, 5) # negative input perimeter

    def test_zero_input(self):
        result = TriangleDef.area(0, 5) # zero input area
        self.assertEqual(result, 0)

        result = TriangleDef.perimeter(0, 5) # zero input perimeter
        self.assertEqual(result, 0)

    def test_float_input(self):
        result = TriangleDef.area(5.5, 5.5) # 5.5*5.5/2
        self.assertEqual(result, 15.125) #float input area

        result = TriangleDef.perimeter(10.5, 10.5) # 10.5 + 10.5 + 10.5
        self.assertEqual(result, 31.5) # float input perimeter

    def test_perimeter_mult(self):
        result = TriangleDef.perimeter(5, 5) # 5 + 5 + 5
        self.assertEqual(result, 15)
    
        result = TriangleDef.perimeter(10, 10) # 10 + 10 + 10
        self.assertEqual(result, 30)

        result = TriangleDef.perimeter(23, 23) # 23 + 23 + 23
        self.assertEqual(result, 69)

        result = TriangleDef.perimeter(200_000, 200_000) # 200_000 + 200_000 + 200_000
        self.assertEqual(result, 600_000)

