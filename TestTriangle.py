# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    """def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')"""

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

""" My additional test cases below """
    def testRightTriangles(self): """test only right triangles"""
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5, 12, 13 is a Right triangle')
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right', '5, 12, 13 is a Right triangle')

    def testIsoscelesTriangles(self): """test only isosceles triangles"""
        self.assertEqual(classifyTriangle(3, 3, 1), 'Isosceles', ' 3, 3, 1 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(8, 8, 2), 'Isosceles', '8, 8, 2 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(16, 16, 17), 'Isosceles', '16, 16, 17 is an Isosceles triangle')

    def testEquilateralTriangle(self): """test equilateral triangles only""""
        self.assertEqual(classifyTriangle(4, 4, 4), 'Equilateral', '4, 4, 4 is an Equilateral triangle')
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 is an Equilateral triangle')
        self.assertEqual(classifyTriangle(20, 20, 20), 'Equilateral', '20, 20, 20 is an Equilateral triangle')

    def testScaleneTraingles(self): """test scalene triangles only""""
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2, 3, 4 is a Scalene triangle')
        self.assertEqual(classifyTriangle(3, 6, 11), 'Scalene', '3, 6, 11 is a Scalene triangle')
        self.assertEqual(classifyTriangle(8, 7, 5), 'Scalene', '8, 7, 5 is a Scalene triangle')

"""    def testOrderOfTriangles(self): """test to see if the order of the sides matters for right and isosceles triangles"""
        self.assertEqual(classifyTriangle(12, 13, 5), 'Right', '12, 13, 5 is a Right triangle')
        self.assertEqual(classifyTriangle(10, 5, 10), 'Isosceles', '10, 5, 10 is an Isosceles triangle')
"""
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
