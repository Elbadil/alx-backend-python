#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class"""
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
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            orgs = GithubOrgClient('google')
            self.assertEqual(orgs.org, mock_org.return_value)
            mock_org.assert_called_once()
            self.assertEqual(orgs._public_repos_url,
                             'https://api.github.com/orgs/google/repos')

    @patch('requests.get')
    def test_public_repos(self, mock_get_request):
        """Tests for the public_repos method"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_property:
            link = 'https://api.github.com/orgs/google/repos'
            mock_property.return_value = link
            mock_resp = Mock()
            orgs = GithubOrgClient('google')
            response_list = [
                {'id': 1936771, 'name': 'truth'},
                {'id': 1936772, 'name': 'autoparse'},
                {'id': 1936773, 'name': 'anvil-build'},
            ]
            mock_resp.json.return_value = response_list
            mock_get_request.return_value = mock_resp
            get_json_resp = orgs.repos_payload
            self.assertEqual(get_json_resp, response_list)
            mock_get_request.assert_called_once()

            repos_list = ['truth', 'autoparse', 'anvil-build']
            get_json_names = orgs.public_repos()
            mock_property.assert_called_once()
            self.assertEqual(repos_list, get_json_names)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license, return_value):
        """Tests for the has_license method"""
        orgs = GithubOrgClient('google')
        result = orgs.has_license(repo, license)
        self.assertEqual(result, return_value)


if __name__ == '__main__':
    unittest.main()
