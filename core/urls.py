from django.urls import path
from .views import Root, About, ContactUs, PackageTrackingDetails, track_page


app_name = 'core'

urlpatterns = [
    path('', Root.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact-us/', ContactUs.as_view(), name='contact_us'),
    path('track/package/', track_page, name='track_package'),
    # path('tracking/<uuid:package_id>/', PackageTrackingDetails.as_view(), name='track')
]
