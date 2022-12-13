from django.shortcuts import render
from django.template.loader import render_to_string



# Create your views here.
from django.http import HttpResponse


def index1(request):
    return HttpResponse("Hello, world. You're at the reports_funnel_summary index.")

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



    html = render_to_string('reports_funnel_summary.html', {'method': method, 'title': title, 'code': code, 'info1': info1, 'info2': info2, 'info3': info3, 'info4': info4, 'info5': info5, 'info6': info6})
    return HttpResponse(html)
