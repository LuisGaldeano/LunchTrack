from django.urls import path
from .views.students_views import student_api_view, student_detail_api_view, student_scholar_year
from .views.classroom_views import classroom_api_view, classroom_detail_api_view


urlpatterns = [
    path('students/', student_api_view, name='students_api'),
    path('students/<int:pk>/', student_detail_api_view, name='student_detail'),
    path('students/scholaryear', student_scholar_year, name='student_scholar_year'),
    path('classrooms/', classroom_api_view, name='classrooms_api'),
    path('classrooms/<int:pk>/', classroom_detail_api_view, name='classrooms_detail'),
]
