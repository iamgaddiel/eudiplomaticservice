from django.urls import path
from .views import Root, About, ContactUs


app_name = 'core'

urlpatterns = [
    path('', Root.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact-us/', ContactUs.as_view(), name='contact_us'),
]