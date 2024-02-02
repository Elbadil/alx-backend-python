#!/usr/bin/env python3
"""Unit tests for utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test for the access_nested_map function with
        parametrized decorator"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self, n_map, path, expected_result):
        """Test for the access_nested_map function with unvalid path key"""
        with self.assertRaises(KeyError, msg=expected_result):
            access_nested_map(n_map, path)


if __name__ == '__main__':
    unittest.main()
