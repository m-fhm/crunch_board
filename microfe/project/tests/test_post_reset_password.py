from unittest.mock import Mock, patch

from nose.tools import assert_is_not_none, assert_list_equal

from project.functions import post_resetpassword


# mocking ok response behavior of api
@patch('project.functions.requests.get')
def test_get_homepage_ssl_mock_response_ok(mock_get):
    mock_get.return_value.ok = True

    response = post_resetpassword()

    assert_is_not_none(response)
