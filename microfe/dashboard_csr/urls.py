from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('resetpassword', views.user_password_reset_through_dashboard, name='reset'),
    path('poll', views.allow_polls_public, name='poll'),
    path('poll_private', views.set_polls_private, name='poll'),
    path('survey', views.get_user_survey_questions, name='get_survey'),
    path('automate', views.user_survey_automation_choise),
    path('logout', views.logout),
]