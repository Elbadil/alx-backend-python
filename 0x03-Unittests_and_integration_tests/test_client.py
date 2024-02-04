#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(
        TEST_PAYLOAD[0][0],
        TEST_PAYLOAD[0][1],
        TEST_PAYLOAD[0][2],
        TEST_PAYLOAD[0][3]
    )]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Setting up the requests.get Mock"""
        cls.get_patcher = patch('requests.get')
        cls.mock_requests_get = cls.get_patcher.start()
        cls.mock_requests_get.side_effect = cls._mock_requests_get

    def test_public_repos(self):
        """tests for the public_repos method with data from fixture.py"""
        google = GithubOrgClient('google')
        result = google.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """tests for the public_repos with license
        method with data from fixture.py"""
        google = GithubOrgClient('google')
        result = google.public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """Stops the patch after all test methods have run"""
        cls.get_patcher.stop()

    @classmethod
    def _mock_requests_get(cls, url):
        """Custom side_effect for requests.get based on different scenarios"""
        split_url = url.split('/')
        if split_url[-1] == 'google':
            return Mock(json=lambda: cls.org_payload)
        elif split_url[-1] == 'repos':
            return Mock(json=lambda: cls.repos_payload)
        else:
            raise ValueError(f"Unexpected URL: {url}")


if __name__ == '__main__':
    unittest.main()
