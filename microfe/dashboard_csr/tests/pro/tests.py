from django.test import TestCase
from dashboard_csr import controller

# Create your tests here.


class resetpassword(TestCase):
    def test_rest_pass(self):
        controller.controller_get_jwt_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyQ29kZSI6IjBtajAyZGQyIiwiZXhwIjoxNjIwNjU4NjIzMjc5fQ.7bp-HYPRATvvasd2FPf8vSVTtVU6xOURN1Q4gUGbSEQ')
        controller.controller_validate_user()
        response = controller.controller_user_password_reset_through_dashboard("joinfa333@yahoo.com").json()

        self.assertEqual(response['err'], {}," response with valid email")        
        
    def test_rest_pass_invalid(self):
        controller.controller_get_jwt_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyQ29kZSI6IjBtajAyZGQyIiwiZXhwIjoxNjIwNjU4NjIzMjc5fQ.7bp-HYPRATvvasd2FPf8vSVTtVU6xOURN1Q4gUGbSEQ')
        controller.controller_validate_user()
        response = controller.controller_user_password_reset_through_dashboard("joinfa333@yacom").json()
        
        self.assertEqual(response['err'], {'status': 'User not found 3'}, "response with invalid email")
