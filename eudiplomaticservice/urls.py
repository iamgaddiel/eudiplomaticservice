from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rt_adm/usr/', admin.site.urls),
    path('back/admin_/', include('custom_admin.urls')),
    path('', include('core.urls'))
]
