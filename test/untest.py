# -*- coding: utf-8 -*-

import unittest


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        print "add"
        pass

    def test_minus(self):
        """Test method minus(a, b)"""
        print "minus"
        pass

    def test_multi(self):
        print "multi"
        """Test method multi(a, b)"""
        pass

    def test_divide(self):
       pass


if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

