#standards libs
from django.shortcuts import render,redirect
import json
from django.template.loader import render_to_string
from django.http import HttpResponse, response

#custom imports from controller.py
from dashboard_csr import controller

def get_jwt_token(request):
    token = request.GET.get('token')
    return_jwt = controller.controller_get_jwt_token(token)
    if return_jwt:
        controller.controller_validate_user()
        return redirect('index')
    else:
        err = "Invalid authentication please login again"
        html = render_to_string('index.html', {'token_error':err})
        return HttpResponse(html)

def logout(request):
    controller.controller_get_jwt_token("pullout")
    return redirect("https://ripe.ai/x10/signin")
def index(request):
    title = 'Reports'
    code = 'X3'
    info1 = request.GET
    info2 = request.POST
    info3 = request.COOKIES
    info4 = request.META
    info5 = request.FILES
    info6 = request.path
    method = request.method
    # # html = render_to_string('dashboard_csr.html', {'method': method, 'title': title, 'code': code, 'info1': info1, 'info2': info2, 'info3': info3, 'info4': info4, 'info5': info5, 'info6': info6})
    # html = render_to_string('dashboard_csr.html',{'code':code, 'title': title})
    # return HttpResponse(html)
    # html = render_to_string('dashboard_csr.html',{'code':code, 'title': title})
    return render(request,'index.html',{'code':code, 'title': title})

def user_password_reset_through_dashboard(request):
    if (request.POST):
        user_mail = request.POST.dict()
        mail = user_mail['user_mail']
        response = controller.controller_user_password_reset_through_dashboard(mail).json()
        print(response)
    # print(response)
        if len(response['err']) != 0:
            # return HttpResponse("please enter proper registed email :" + response['err']['status'])
            err = response['err']['status']
            html = render_to_string('reset_pass.html', {'error':err})
            return HttpResponse(html)
        else:
            
            html = render_to_string('reset_pass.html', {'mail':mail})
            return HttpResponse(html)
            # return redirect('index')
    else:
         return render(request,'reset_pass.html')

    
# allow to go polls public by csr 
def allow_polls_public(request):
    if (request.POST):
        form_post = request.POST.dict()
        pollid = form_post['pollid']
        response = controller.controller_allow_polls_public(pollid).json()
        print(response)
        if(response):
            html = render_to_string('publicise_poll.html', {'poll':pollid})
            return HttpResponse(html)
        else:
            err = "something goes wrong please contact admin"
            html = render_to_string('publicise_poll.html', {'error':err})
            return HttpResponse(html)
    else:
        html = render_to_string('publicise_poll.html')
        return HttpResponse(html)

def set_polls_private(request):
    if (request.POST):
        form_post = request.POST.dict()
        pollid = form_post['pollid']
        response = controller.controller_set_polls_private(pollid).json()
        print(response)
        if(response):
            html = render_to_string('private_poll.html', {'poll':pollid})
            return HttpResponse(html)
        else:
            err = "something goes wrong please contact admin"
            html = render_to_string('private_poll.html', {'error':err})
            return HttpResponse(html)
    else:
        html = render_to_string('private_poll.html')
        return HttpResponse(html)
    
def get_user_survey_questions(request):
    if (request.POST):
        form_post = request.POST.dict()
        global surveyid
        surveyid = form_post['surveyid']
        response = controller.controller_get_user_survey_questions(surveyid).json()
        # print(type(json.loads(response['surveyObject'])))
        global survey_data
        survey_data = json.loads(response['surveyObject'])

        # questions = {}
        # for chunks in survey_data:
        #     # print(chunks)
        #     questions[chunks['id']] = chunks
        #     # print(chunks['name'])



        # print(survey_data)
        # map_survey_object = []
        # head1=""
        # for n in survey_data:
        #     print(n)
        #     if n['type']=="header-h1":
        #         head1 = n['name']
        #     if n['type']=="select":
        #         select_name = n['name']
        #         map_survey_object.append(n['value'])
        #         # print(type(n['value']))
        
        # print(map_survey_object,"head:",head)
        # return render(request,'dashboard_csr.html',{'data':map_survey_object,'heading':head1,'select_name':select_name})
        # print(survey_data)
        return render(request,'survey_choices.html',{'quest':survey_data})
    else:
        return render(request,'survey.html')

def user_survey_automation_choise(request):
    # print(survey_data)
    form_post = request.POST.dict()
    # print(form_post)
    for n in survey_data:
        # print(n)
        if 'value' in n:
            for inner in n['value']:
                for form_retun in form_post:
                    # print(form_retun)
                    sub_s = "_"+ n['questionCode']
                    if sub_s in form_retun and inner['label'] in form_retun:
                        inner['automation_choise']=form_post[form_retun]
                # print(inner)
        
        #  # ################### this part attach automate object with corresponding question 
        # automateObject= {}
        # if n['questionCode'] in form_post:
        #     # print(n['questionCode'])
        #     key = list(form_post.keys()).index(n['questionCode'])+1
        #     get_next_key= list(form_post)
        #     # print(get_next_key[key])
        #     # print(form_post[n['questionCode']])

        #     automateObject['choise'] = form_post[n['questionCode']]
        #     automateObject['quantity'] = form_post[get_next_key[key]]
        #     n["automateObject"] = automateObject
    
    survey_code = {}
    survey_code['survey_id'] = surveyid
    # automateObject['user_automate_choices'] = form_post
    survey_data.append(survey_code)
    

        # if n['type']=="select":
        #     select_name = n['name']
        #     map_survey_object.append(n['value'])
            # print(type(n['value']))
    print(survey_data)
    response = controller.post_automate_object(survey_data).json()
    if response['success']==True:
        return render(request,"survey.html",{'success':'Submited Successfuly'})
    else:
        return render(request,"survey.html",{'error':'Submition failed please try again'})
    # return redirect('get_survey')
