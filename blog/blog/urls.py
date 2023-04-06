

from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("LeBlog.urls")),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include("members.urls")),
]+ static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT) #pour immage

