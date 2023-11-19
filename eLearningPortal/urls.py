from . import views
from django.urls import path

app_name = 'eLearningPortal'

urlpatterns = [
    path('',views.index, name='index'),
]