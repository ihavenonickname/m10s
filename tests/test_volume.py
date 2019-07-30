import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from m10s import volume, M10SException

class TestVolumeFunctions(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(1e+6, volume.convert(1, 'm³', 'cm³'))
        self.assertEqual(1, volume.convert(1000000, 'cm³', 'm³'))
        self.assertEqual(1e-6, volume.convert(1, 'cm³', 'm³'))

    def test_convert_si(self):
        self.assertEqual(1, volume.convert_si(1000000, 'cm³'))
        self.assertEqual(1, volume.convert_si(1, 'm³'))

    def test_bad_units(self):
        with self.assertRaises(M10SException):
            volume.convert(1, 'm³', 'g')

        with self.assertRaises(M10SException):
            volume.convert(1, 'cm', 'm³')

        with self.assertRaises(M10SException):
            volume.convert_si(1, 'm²')

