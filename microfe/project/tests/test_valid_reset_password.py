from unittest.mock import Mock, patch
from dashboard_csr import controller
from nose.tools import assert_is_not_none, assert_list_equal, assertEqual
from project.functions import post_resetpassword

# import email_ID


# mocking ok response behavior of api
@patch('project.functions.requests.get')
def test_get_valid_resetpassword(mock_get):
    
    email_ID = "sabaaltaf0092@gmail.com"
 

    mock_get.return_value.ok = True

    controller.controller_get_jwt_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyQ29kZSI6IjBtajAzaWNjIiwiZXhwIjoxNjIwNDg2NTkyNDEwfQ.phiDIEiKpKfYz7zZS6LyTGUxjilE9ZwexDSsGF0SYdI')
    controller.controller_validate_user()
    response = post_resetpassword(email_ID).json()
    # response = response.json

    .assertEqual(response['err'], {}, "response with valid email")

    # print(test_get_valid_resetpassword())  

    # assert_is_not_none(response)




# def test_post_valid_resetpassword():
#     email = "sabaaltaf0092@gmail.com"
#     response = post_resetpassword(email)

#     if response['err'] == {}:
#         return True


#     else: 
#         return False

# print(test_post_valid_resetpassword())       


