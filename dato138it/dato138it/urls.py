from django.conf.urls.static import static
from django.contrib import admin
from dato138it import settings
from django.urls import path, include
from progress.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('progress.urls')),
	path('captcha/', include('captcha.urls')),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = pageNotFound