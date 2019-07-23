import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sv_converter import mass, SVConverterException

class TestMassFunctions(unittest.TestCase):
    def test_convert_Mg(self):
        self.assertEqual(1000, mass.convert(1, 'Mg', 'kg'))
        self.assertEqual(1e+6, mass.convert(1, 'Mg', 'g'))
        self.assertEqual(1e+9, mass.convert(1, 'Mg', 'mg'))

    def test_convert_kg(self):
        self.assertEqual(0.001, mass.convert(1, 'kg', 'Mg'))
        self.assertEqual(1000, mass.convert(1, 'kg', 'g'))
        self.assertEqual(1e+6, mass.convert(1, 'kg', 'mg'))

    def test_convert_g(self):
        self.assertEqual(1e-6, mass.convert(1, 'g', 'Mg'))
        self.assertEqual(0.001, mass.convert(1, 'g', 'kg'))
        self.assertEqual(1000, mass.convert(1, 'g', 'mg'))

    def test_convert_mg(self):
        self.assertEqual(1e-9, mass.convert(1, 'mg', 'Mg'))
        self.assertEqual(1e-6, mass.convert(1, 'mg', 'kg'))
        self.assertEqual(1e+6, mass.convert(1, 'mg', 'ng'))

    def test_convert_ug(self):
        self.assertEqual(1e-12, mass.convert(1, 'ug', 'Mg'))
        self.assertEqual(1e-9, mass.convert(1, 'ug', 'kg'))
        self.assertEqual(1000, mass.convert(1, 'ug', 'ng'))

    def test_convert_ng(self):
        self.assertEqual(1e-15, mass.convert(1, 'ng', 'Mg'))
        self.assertEqual(1e-12, mass.convert(1, 'ng', 'kg'))
        self.assertEqual(1e-9, mass.convert(1, 'ng', 'g'))

    def test_convert_si(self):
        self.assertEqual(1000, mass.convert_si(1, 'Mg'))
        self.assertEqual(1, mass.convert_si(1, 'kg'))
        self.assertEqual(0.001, mass.convert_si(1, 'g'))

    def test_bad_units(self):
        with self.assertRaises(SVConverterException):
            mass.convert(1, 'kg', 'padmé')

        with self.assertRaises(SVConverterException):
            mass.convert(1, 'master yoda', 'g')

        with self.assertRaises(SVConverterException):
            mass.convert_si(1, 'hello there')
