from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html',
                  {'students': students})


def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            roll_number=request.POST['roll_number'],
            department=request.POST['department'],
            email=request.POST['email']
        )
        return redirect('student_list')
    return render(request, 'students/student_form.html')


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.roll_number = request.POST['roll_number']
        student.department = request.POST['department']
        student.email = request.POST['email']
        student.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html',
                  {'student': student})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html',
                  {'student': student})
                  