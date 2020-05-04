from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('chat/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
