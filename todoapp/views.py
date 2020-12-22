from django.shortcuts import render
from django.utils import timezone
from todoapp.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'main/index.html', {
        'todo_items' : todo_items
    } )
def add_todo(request):
    content = request.POST.get('content')
    current_date = timezone.now()
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    len_of_todos = Todo.objects.all().count()
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")


