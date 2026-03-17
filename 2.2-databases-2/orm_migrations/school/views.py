from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student

def student_list(request):
    students = Student.objects.prefetch_related('teachers').all()
    return render(request, 'school/students_list.html', {'students': students})

def redirect_to_students(request):
    return redirect('students')  # name='students' из urls.py