from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    all_todo = Todo.objects.filter(author = request.user).order_by('-pk')
    context = {'all_todo':all_todo}
    return render(request, 'todo/home.html', context)

def addTodo(request):
    todo_obj = request.POST['content']
    todo_title = request.POST['title']
    if todo_obj != '':
        title = todo_obj
        content = todo_title
        Todo(title=title,  content=content, author=request.user).save()
    return redirect('home')
    

def deleteTodo(request, item_id):
    todo_item = Todo.objects.get(pk=item_id)
    todo_item.delete()
    return redirect('home')
    

def mark_as_complete(request):
    post_list = Todo.objects.all()
    if request.user.is_superuser:
        if request.method == 'POST':
            id_list = request.POST['boxes']
            post_list.update(status = False)
            for x in id_list:
                Todo.objects.filter(pk = int(x)).update(status= True)
            messages.success(request, ('Task completed'))
            return redirect('home')
    return redirect('home')