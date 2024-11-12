from django.urls import path
from .views import home,question_view,submit_answer,results_view

urlpatterns = [
    path('',home, name='home'),
    path('questions/',question_view, name='questions'),
    path('submit_answer/',submit_answer, name='submit_answer'),
    path('results/',results_view, name='results_view'),
]