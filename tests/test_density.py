import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from m10s import density

class TestDensityFunctions(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(1000, density.convert(1, 'g/cm3', 'kg/m3'))
        self.assertEqual(0.001, density.convert(1, 'g/cm3', 'kg/cm3'))
        self.assertEqual(1000, density.convert(1, 'kg/m3', 'g/m3'))
        self.assertEqual(1000000, density.convert(1, 'kg/cm3', 'kg/m3'))

    def test_convert_si(self):
        self.assertEqual(1, density.convert_si(1, 'kg/m3'))
        self.assertEqual(1000, density.convert_si(1, 'g/cm3'))
