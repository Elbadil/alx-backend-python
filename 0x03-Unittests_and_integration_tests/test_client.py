#!/usr/bin/env python3
"""Unit tests for client.py"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the class GithubOrgClient"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('requests.get')
    def test_org(self, org_name, mock_get_request):
        """"""
        mock_resp = Mock()
        orgs = GithubOrgClient(org_name)
        response_dict = {'name': 'Adil', 'age': 26}
        mock_resp.json.return_value = response_dict
        mock_get_request.return_value = mock_resp

        get_json_data = orgs.org
        mock_get_request.assert_called_with(
            GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(get_json_data, response_dict)


if __name__ == '__main__':
    unittest.main()
