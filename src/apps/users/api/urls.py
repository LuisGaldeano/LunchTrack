from django.urls import path
from .views.user_views import user_api_view, user_detail_api_view

urlpatterns = [
    path('users/', user_api_view, name='user_api'),
    path('users/<int:pk>/', user_detail_api_view, name='user_detail_api'),
]
