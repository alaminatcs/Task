from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(request):
    emp = models.Employee.objects.all()
    return render(request, 'emp_home.html', {'data': emp})

def remove_emp(request, id):
    models.Employee.objects.get(pk = id).delete()
    return redirect('emp')