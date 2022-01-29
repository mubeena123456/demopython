from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from . models import Todo
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class TaskListView(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'task1'

class TaskDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'task1'

class TaskUpdateView(UpdateView):
    model = Todo
    template_name = 'edit.html'
    fields = ['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def index(request):
    task1=Todo.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Todo(name=name,priority=priority,date=date)
        task.save()
    return render(request,'index.html',{'task1':task1})

def update(request,id):
    task=Todo.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})

def delete(request,id):
    task=Todo.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

