#!/usr/bin/env python3
"""Unit tests for client.py"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the class GithubOrgClient"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('requests.get')
    def test_org(self, org_name, mock_get_request):
        """Tests for the org method using parameterized and patch"""
        mock_resp = Mock()
        orgs = GithubOrgClient(org_name)
        response_dict = {'name': 'Adil', 'age': 26}
        mock_resp.json.return_value = response_dict
        mock_get_request.return_value = mock_resp

        get_json_data = orgs.org
        mock_get_request.assert_called_with(
            GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(get_json_data, response_dict)

    def test_public_repos_url(self):
        """Tests for the _public_repos_url property"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'name': 'google',
                'repos_url': 'https://api.github.com/orgs/google/repos_url'
                }
            orgs = GithubOrgClient('google')
            self.assertEqual(orgs.org, mock_org.return_value)
            mock_org.assert_called_once()
            self.assertEqual(orgs._public_repos_url,
                             'https://api.github.com/orgs/google/repos_url')


if __name__ == '__main__':
    unittest.main()
