from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
def index(request):
    data_save=TaskForm()
    if request.method=='POST':
        data_save=TaskForm(request.POST,request.FILES)
        if data_save.is_valid():
            data_save.save()
            return redirect('/')
    context={
        'tasks':Task.objects.all(),
        'form':data_save
    }
    return render(request,'pages/index.html',context)
