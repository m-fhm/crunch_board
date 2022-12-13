from urllib.parse import urljoin
from datetime import datetime
import requests
import calendar
import json
import jwt
#custom imports
from django.http import HttpResponse

def controller_get_jwt_token(token):
    # global jwt_token , userCode , valid_user
    # jwt_token = token
    # payload = jwt.decode(token, "ertugrul2020", algorithms=["HS256"])
    # userCode = payload['userCode']
    # return userCode
    try:
        global jwt_token , userCode , valid_user
        jwt_token = token
        payload = jwt.decode(token , "ertugrul2020", algorithms=["HS256"])
        userCode = payload['userCode']
        time_utc=calendar.timegm(datetime.utcnow().utctimetuple())*1000
        if payload['exp'] < time_utc:
            raise Exception("token expire")
        # decoded = json.loads(json.dumps(jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)))
        return userCode
    except:
        print("expire")

def controller_validate_user():
    
    if controller_get_jwt_token(jwt_token):
        global valid_user
        valid_user = False
        user_validate_url = "http://api.ripe.ai/api/2.0/users/"+userCode+"/validate"
        headers = {
            'clientid': "12121212",
            'authorization': "bearer "+ jwt_token,
        }
        response_user_validate = requests.request("POST", url=user_validate_url, headers=headers).json()
        # print(type(response_user_validate))
        # print(response_user_validate)
        user_plan_type= response_user_validate['data']['user']['planType']
        
        
        if user_plan_type=="csradmin" or user_plan_type=="betatester" or user_plan_type=="superadmin":
            valid_user = True 
        return valid_user

def controller_user_password_reset_through_dashboard(mail):
    if controller_get_jwt_token(jwt_token):
        url = "http://api.ripe.ai/api/1.0/users/ripe/resetpassword"
        data = "email="+mail
        # print(da
        headers = {
        'clientid': "12121212",

        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        }
        response = ""
        if valid_user == True:    
            response=requests.request("POST", url, data=data, headers=headers)
        else:
            return HttpResponse("your are not the valid user to perform this operation please contact admin")
        return response   

# allow to go polls public by csr 
def controller_allow_polls_public(pollid):
    if controller_get_jwt_token(jwt_token):
        base_url = "http://api.ripe.ai/api/2.0/poll/"
        md_url =  userCode+ "/" +pollid+ "/state/public"
        url = urljoin(base_url,md_url)
        headers = {
        'clientid': "12121212",
        'authorization': "bearer "+ jwt_token,
        }
        response = ""
        if valid_user == True:
            response = requests.request("POST", url, headers=headers)
        else:
            return HttpResponse("your are not the valid user to perform this operation please contact admin")

        return response

# allow to go polls public by csr 
def controller_set_polls_private(pollid):
    if controller_get_jwt_token(jwt_token):
        base_url = "http://api.ripe.ai/api/2.0/poll/"
        md_url =  userCode+ "/" +pollid+ "/state/private"
        url = urljoin(base_url,md_url)
        headers = {
        'clientid': "12121212",
        'authorization': "bearer "+ jwt_token,
        }

        response = ""
        if valid_user == True:
            response = requests.request("POST", url, headers=headers)
        else:
            return HttpResponse("your are not the valid user to perform this operation please contact admin")
        return response   

def controller_get_user_survey_questions(surveyid):
    if controller_get_jwt_token(jwt_token):    
        base_url = "http://api.ripe.ai/api/2.0/survey/"
        md_url = userCode+"/"+ surveyid
        url = urljoin(base_url,md_url)
        headers = {
        'clientid': "1209487",
        'authorization': "bearer "+jwt_token,
        }
        response = ""
        
        if valid_user == True:
            
            response = requests.request("POST", url, headers=headers)
        else:
            
            return HttpResponse("your are not the valid user to perform this operation please contact admin")
            
        return response
    
def post_automate_object(automate_object):
    if controller_get_jwt_token(jwt_token):    
        automate_object = str(automate_object)
        url = "http://api.ripe.ai/api/2.0/automation/"+userCode
        querystring = {"object":"survey"}
        headers = {
        'clientid': "1209487",
        'authorization': "bearer "+jwt_token,
        'ripeobject':automate_object
        }
        response = ""
        if valid_user == True:
            response = requests.request("POST", url, headers=headers, params=querystring)
        else:
            return HttpResponse("your are not the valid user to perform this operation please contact admin")
        return response
