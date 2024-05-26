#!/usr/bin/env python3
'''Test utils'''
import unittest
from utils import access_nested_map
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

    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: List,
                                         expected: Any) -> None:
        '''Tests exceptions for access_nested_map'''
        self.assertRaises()


if __name__ == '__main__':
    unittest.main()
