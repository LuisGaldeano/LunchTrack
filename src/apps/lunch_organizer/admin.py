from django.contrib import admin
from .models.classroom import Classroom
from .models.student import Student

admin.site.register(Classroom)
admin.site.register(Student)