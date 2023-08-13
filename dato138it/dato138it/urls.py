from django.conf.urls.static import static
from django.contrib import admin
from dato138it import settings
from django.urls import path, include
from portfolio.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')), #http://127.0.0.1:8000/portfolio/
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = pageNotFound