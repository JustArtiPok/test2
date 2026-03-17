from django.urls import path
from school.views import student_list, redirect_to_students

urlpatterns = [
    path('student/list/', student_list, name='students'),
    path('', redirect_to_students, name='home'),
]
