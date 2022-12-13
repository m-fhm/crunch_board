

from django.shortcuts import render
from django.template.loader import render_to_string
import requests
from datetime import datetime
from django.http import HttpResponse

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    return text


def index(request):
    print("reports_shortcode_analytics.1")
    title = 'Reports'
    code = 'X3'
    info1 = "" # request.GET
    info2 = "" # request.POST
    info3 = "" # request.COOKIES
    info4 = "" # request.META
    info5 = "" # request.FILES
    info6 = "" # request.path
    info7 = ""
    info8 = ""
    method = "" # request.method
    AFFILIATE_VALUE = 1 # $


    parameters = {
        
    }

    # SAMPLE
    # FYI: for reset password
    # https://api.ripe.ai:8080/api/1.0/users/ripe/resetpassword
    # BODY: 
    # email: <user email>
    # CLIENTID: 12121212
    # POST  (request.post)


    response = requests.get(
        # "http://api.ripe.ai/api/1.0/traces/shortcodes",
        "https://api.ripe.ai/api/1.0/users/ripe/resetpassword", 
        # "http://localhost:8080/api/1.0/traces/shortcodes", 
        params=parameters,
        headers={'Content-Type':'application/json', 'CLIENTID': '1312313'}
        )


    # print("reports_shortcode_analytics.2")
    # jprint(response.json())
    summary = response.json()['data']['summary']
    # ['users']['affiliates']
    # print(summary)
    traces = []

    jprint(summary);

    html = render_to_string('reports_shortcode_analytics.html', {'method': method, 'title': title, 'code': code, 'traces': traces, 'summary': summary, 'usernames': summary["usernames"], 'months': summary["months"], 'shortcodes': summary["shortcodes"], 'daysOfWeek': summary["dayOfWeek"], 'info5': info5, 'info6': info6, 'info7': info7, 'info8': info8})


    return HttpResponse(html)