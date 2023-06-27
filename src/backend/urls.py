from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.lunch_organizer.api.urls')),
    path('', include('apps.users.api.urls')),
]
