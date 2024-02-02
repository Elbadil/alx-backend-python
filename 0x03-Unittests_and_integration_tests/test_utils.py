#!/usr/bin/env python3
"""Unit tests for utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """Tests for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, get_request):
        """Tests for the get_json function using the Mock Object"""
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload

        get_request.return_value = mock_resp
        get_url_json = get_json(test_url)
        get_request.assert_called_once_with(test_url)
        self.assertEqual(get_url_json, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator"""

    def test_memoize(self):
        """Tests for the memoize decorator on a TestClass"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            obj = TestClass()
            result1 = obj.a_property
            result2 = obj.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
