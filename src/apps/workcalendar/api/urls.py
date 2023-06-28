from django.urls import path
from .views.workcalendar_views import workcalendar_api_view, workcalendar_download_api_view


urlpatterns = [
    path('calendar/', workcalendar_api_view, name='workcalendar_api'),
    path('calendar/download/', workcalendar_download_api_view, name='workcalendar_download_api'),
]