import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sv_converter import length, SVConverterException

class TestLengthFunctions(unittest.TestCase):
    def test_convert_km(self):
        self.assertEqual(1000, length.convert(1, 'km', 'm'))
        self.assertEqual(100000, length.convert(1, 'km', 'cm'))
        self.assertEqual(1e+12, length.convert(1, 'km', 'nm'))

    def test_convert_m(self):
        self.assertEqual(0.001, length.convert(1, 'm', 'km'))
        self.assertEqual(100, length.convert(1, 'm', 'cm'))
        self.assertEqual(1e+9, length.convert(1, 'm', 'nm'))

    def test_convert_dm(self):
        self.assertEqual(0.0001, length.convert(1, 'dm', 'km'))
        self.assertEqual(10, length.convert(1, 'dm', 'cm'))
        self.assertEqual(1e+8, length.convert(1, 'dm', 'nm'))

    def test_convert_cm(self):
        self.assertEqual(0.00001, length.convert(1, 'cm', 'km'))
        self.assertEqual(0.1, length.convert(1, 'cm', 'dm'))
        self.assertEqual(1e+7, length.convert(1, 'cm', 'nm'))

    def test_convert_mm(self):
        self.assertEqual(1e-6, length.convert(1, 'mm', 'km'))
        self.assertEqual(0.1, length.convert(1, 'mm', 'cm'))
        self.assertEqual(1e+6, length.convert(1, 'mm', 'nm'))

    def test_convert_um(self):
        self.assertEqual(1e-9, length.convert(1, 'um', 'km'))
        self.assertEqual(1e-4, length.convert(1, 'um', 'cm'))
        self.assertEqual(1000, length.convert(1, 'um', 'nm'))

    def test_convert_nm(self):
        self.assertEqual(1e-12, length.convert(1, 'nm', 'km'))
        self.assertEqual(1e-9, length.convert(1, 'nm', 'm'))
        self.assertEqual(1e-7, length.convert(1, 'nm', 'cm'))

    def test_convert_si(self):
        self.assertEqual(1000, length.convert_si(1, 'km'))
        self.assertEqual(1, length.convert_si(1, 'm'))
        self.assertEqual(0.01, length.convert_si(1, 'cm'))

    def test_bad_units(self):
        with self.assertRaises(SVConverterException):
            length.convert(1, 'cm', 'anakin skywalker')

        with self.assertRaises(SVConverterException):
            length.convert(1, 'ahsoka tano', 'km')

        with self.assertRaises(SVConverterException):
            length.convert_si(1, 'this is so wizard!')

