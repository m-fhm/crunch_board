
from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import admin
from django.urls import include, path
from dashboard_csr import views
DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            './templates/'
        ],
    },
]


def home(request):
    color = request.GET.get('color', '')
#     return HttpResponse('<h1 style="color:' + color + '">Welcome!</h1><hr><p><a href="/about/">About</a></p>')
    title = 'Reports'
    code = 'X3'
    html = render_to_string('index.html', {'title': title, 'code': code})
    return HttpResponse(html)

def about(request):
    title = 'Reports'
    code = 'X3'
    html = render_to_string('about.html', {'title': title, 'code': code})
    return HttpResponse(html)
def survey(request):
    html = render_to_string('survey.html')
    return HttpResponse(html)

urlpatterns = [
    url(r'^$',include('dashboard_csr.urls')),
    url(r'^about/$', about, name='aboutpage'),
    url(r'^csrdashboard/$',views.get_jwt_token, name='token'),

    path('reports_funnel_summary/', include('reports_funnel_summary.urls')),
    path('dashboard_csr/', include('dashboard_csr.urls')),
    # path('reportsUI/', include('reportsUI.urls')),

]


