from django.urls import path
from .views import Root


app_name = 'core'

urlpatterns = [
    path('', Root.as_view(), name='index')
]