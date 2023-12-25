from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('rt_adm/usr/', admin.site.urls),
    path('back/admin_/', include('custom_admin.urls')),
    path('', include('core.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'core.views.handle_404_request'
# handler500 = 'core.views.handle_500_request' 