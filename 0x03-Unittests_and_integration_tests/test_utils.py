#!/usr/bin/env python3
'''Test utils'''
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from typing import Mapping, List, Union, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''Test utils'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: List,
                               expected: Any) -> None:
        '''Test access_nested_map'''
        self.assertAlmostEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: List,
                                         expected: Any) -> None:
        '''Tests exceptions for access_nested_map'''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Test GetJson'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self,
                      test_url: str,
                      test_payload: dict):
        '''Test get_json'''
        attrs = {'json.return_value': test_payload}

        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
