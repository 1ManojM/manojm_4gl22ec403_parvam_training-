from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm
from django.contrib import messages

# Create your views here.
def teacher_list(request):
    return render(request, 'teacher_crud/teacher_list.html',)

def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Teacher details added successfully')
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher_crud/create_teacher.html')   

def view_teacher(request):
    return render(request, 'teacher_crud/view_teacher.html')   

def edit_teacher(request):
    return render(request, 'teacher_crud/edit_teacher.html')   

def delete_teacher(request):
    return render(request, 'teacher_crud/delete_teacher.html')   