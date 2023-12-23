from django.urls import path
from .views import Root, About, ContactUs, track_page, TermsAndCondition, PrivacyPolicy


app_name = 'core'

urlpatterns = [
    path('', Root.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact-us/', ContactUs.as_view(), name='contact_us'),
    path('tc/', TermsAndCondition.as_view(), name='terms_and_condition'),
    path('privacy-policy/', PrivacyPolicy.as_view(), name='privacy'),
    path('track/package/', track_page, name='track_package'),
]
