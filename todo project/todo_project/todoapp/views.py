from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView


# Create your views here.


class Tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='tasks'
    
class DetailView(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='tasks'
    

    
class Taskdeleteview(DeleteView):
    model=Task
    template_name='home.html'
    success_url=reverse_lazy('cbvhome')
    
      

def home(request):
    tasks=Task.objects.all()
    if request.method=='POST':
        task=request.POST.get('task','')
        date=request.POST.get('date','')
       
        
        task_add_db=Task(task=task,date=date)
        task_add_db.save()
   
    
        
    return render(request,'home.html',{'tasks':tasks})



def delete(request,id):
    delete_object=Task.objects.get(id=id)
    delete_object.delete()
    
    return redirect('/')

def edit(request,id):
    
    instancd_edit=Task.objects.get(id=id)
    if request.method=='POST':
        taskname=request.POST.get('task')
        date=request.POST.get('date')
        instancd_edit.task=taskname
        instancd_edit.date=date
        instancd_edit.save()
        return redirect('/')
    return render(request,'home.html',{'task':instancd_edit.task,'date':instancd_edit.date})
    

        
    
    
    