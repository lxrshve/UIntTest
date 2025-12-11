import unittest
import math
import rectangle
import square
import triangle
import circle

class TestRectangle(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(rectangle.area(5), math.pi * 25)  # 25 * pi
    
    def test_area_edge(self):
        self.assertEqual(rectangle.area(0), 0)  # 0 * 0 * pi = 0
    
    def test_perimeter_normal(self):
        self.assertEqual(rectangle.perimeter(5), 2 * math.pi * 5)  # 2 * pi * 5
    
    def test_perimeter_edge(self):
        self.assertEqual(rectangle.perimeter(-10), 2 * math.pi *(-10))  # 2 * pi * -10

class TestSquare(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(square.area(5), 25)  # 5² = 25
    
    def test_area_edge(self):
        self.assertEqual(square.area(0), 0)   # 0² = 0
    
    def test_perimeter_normal(self):
        self.assertEqual(square.perimeter(5), 20)  # 4*5 = 20
    
    def test_perimeter_edge(self):
        self.assertEqual(square.perimeter(0), 0)   # 4*0 = 0

class TestTriangle(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(triangle.area(6, 4), 12)  # (1/2)*6*4 = 12
    
    def test_area_edge(self):
        self.assertEqual(triangle.area(0, 5), 0)   # (1/2)*0*5 = 0
    
    def test_perimeter_normal(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)  # 3+4+5 = 12
    
    def test_perimeter_edge(self):
        self.assertEqual(triangle.perimeter(0, 4, 5), 9)   # 0+4+5 = 9

class TestCircle(unittest.TestCase):
    def test_area_normal(self):
        self.assertAlmostEqual(circle.area(3), math.pi * 9)  # π*3² ≈ 28.27
    
    def test_area_edge(self):
        self.assertEqual(circle.area(0), 0)  # π*0² = 0
    
    def test_perimeter_normal(self):
        self.assertAlmostEqual(circle.perimeter(3), 2 * math.pi * 3)  # 2π*3 ≈ 18.85
    
    def test_perimeter_edge(self):
        self.assertEqual(circle.perimeter(0), 0)  # 2π*0 = 0

