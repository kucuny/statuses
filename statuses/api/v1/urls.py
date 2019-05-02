from django.urls import path

from statuses.api.v1 import views


app_name = 'v1'
urlpatterns = [
    path('test/', views.t, name='test'),
]
