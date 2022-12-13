'''
File containing all functions as services

'''

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

from dashboard_csr.controller import controller_user_password_reset_through_dashboard

try:
    import tests.urls as u    # this way of import works for nosetests lib so ignore pylint error
except ModuleNotFoundError:
    import urls as u



### GET functions

def post_resetpassword(email_ID):
    # build
    # change variable here

    print(email_ID)

    # call  
    response = controller_user_password_reset_through_dashboard(email_ID)
<<<<<<< HEAD:microfe/project/functions.py
=======

    print(response.json())

>>>>>>> saba_dev:microfe/tests/functions.py

    # extract

    if response.ok:
        # print(response.json())
        return response
    else:
        return None

### POST functions


def post_sign_up_no_ssl(email_ID, client_ID):
    # email_ID -> str; client_ID -> int

    URL_SIGN_UP_NO_SSL = urljoin(u.NO_SSL + u.BASE_SIGN_UP, email_ID)

    response = requests.post(URL_SIGN_UP_NO_SSL, data={ 'CLIENTID' : str(client_ID) })

    if response.ok:
        print(response.json())
        return response
    else:
        return None


def post_sign_up_ssl(email_ID, client_ID):
    # email_ID -> str; client_ID -> int

    URL_SIGN_UP_SSL = urljoin(u.SSL + u.BASE_SIGN_UP, email_ID)

    response = requests.post(URL_SIGN_UP_SSL, data={ 'CLIENTID' : str(client_ID) })

    if response.ok:
        print(response.json())
        return response
    else:
        return None



if __name__ == "__main__":
    email_ID = 'nov18@ripe.ai'

    client_ID = 1312313

    post_sign_up_no_ssl(email_ID, client_ID)

    print(post_invalid_email_no_ssl_check('random@r.com', client_ID))
    print(post_invalid_email_no_ssl_check('muhammadahmed10b@gmail.com', client_ID))