"""Test module for pbs client."""
import pbclient
from helpers import *
from mock import patch
from nose.tools import assert_raises
from requests import exceptions


class Test(object):

    """Test class for pbs."""

    @patch('pbclient.find_app')
    def test_find_app_by_short_name(self, mock):
        """Test find_app_by_short_name returns a project."""
        mock.return_value = ['project']
        project = find_app_by_short_name('project', pbclient)
        err_msg = "It shoul return: project"
        assert project == 'project', err_msg

    @patch('pbclient.find_app')
    def test_find_app_by_short_name_connection_error(self, mock):
        """Test find_app_by_short_name connection_error is raised."""
        mock.side_effect = exceptions.ConnectionError
        assert_raises(exceptions.ConnectionError,
                      find_app_by_short_name,
                      'project',
                      pbclient)

    @patch('helpers.format_error')
    @patch('pbclient.find_app')
    def test_find_app_by_short_name_error(self, mock, mock2):
        """Test find_app_by_short_name error is printed."""
        error = {"action": "GET",
                 "exception_cls": "NotFound",
                 "exception_msg": "(NotFound)",
                 "status": "failed",
                 "status_code": 404,
                 "target": "/api/app"}
        mock.return_value = error
        find_app_by_short_name('project', pbclient)
        mock2.assert_called_with('pbclient.find_app', error)