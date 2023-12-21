from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    DashboardView,
    ListPackages,
    DetailView,
    CreatePackage,
    PackageDetail,
    ListHistory,
    CreateShipmentHistory,
    logout_view
)

app_name = 'custom_admin'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(template_name='custom_admin/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('pakages/', ListPackages.as_view(), name='package_list'),
    path('pakages/<uuid:pk>/', DetailView.as_view(), name='package_detail'),
    path('pakages/create/', CreatePackage.as_view(), name='package_create'),
    path('pakage/<uuid:pk>/', PackageDetail.as_view(), name='package_detail'),
    path('history/<uuid:pk>', ListHistory.as_view(), name='history_list'),
    path('history/create/', CreateShipmentHistory.as_view(), name='history_create'),
]
