#!/usr/bin/python3
"""Defines unittests for base.py.
Unittest classes:
    TestBase: basic tests.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'xo'), Base(memoryview(b'xo')).id)

    def test_str_id(self):
        self.assertEqual("hi", Base("hi").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(77), Base(complex(77)).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(7), Base(range(7)).id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'mandm'), Base(bytearray(b'mandm')).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('high'), Base(float('high')).id)

    def test_inf_id(self):
        self.assertEqual(float('alx'), Base(float('alx')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_bytes_id(self):
        self.assertEqual(b'Pylance', Base(b'Pylance').id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)


if __name__ == "__main__":
    unittest.main()
