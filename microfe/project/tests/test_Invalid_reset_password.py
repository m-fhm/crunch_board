# from unittest.mock import Mock, patch

# from nose.tools import assert_is_not_none, assert_list_equal

# from project.functions import post_resetpassword

# # import email_ID


# # mocking ok response behavior of api
# @patch('project.functions.requests.get')
# def test_get_Ivalid_resetpassword(mock_get):

#     email_ID = "xyz@random.com"
 

#     mock_get.return_value.ok = True

#     response = post_resetpassword(email_ID)

#     if response['err']['status'] == 'User not found 3':

#         return True

#     else: 
#         return False

# # print(test_get_Invalid_resetpassword())  

# assert_is_not_none(response)




# # def test_post_Invalid_resetpassword():
# #     email = "xyz@randon.com"
# #     response = post_resetpassword(email)

# #     if response['err']['status'] == 'User not found 3':

# #         return True


# #     else: 
# #         return False

# # print(test_post_Invalid_resetpassword())  
      


