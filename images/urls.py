from django.urls import path
from . import views


app_name = 'images'

urlpatterns = [
        path('', views.top_page, name='top_page'),
        path('form/', views.form_page, name='form_page'),
]

