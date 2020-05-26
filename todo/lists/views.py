from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import TodoItem,User

#add todo item to the existing user

#create new todo item
def create_todo_item(request):
    new_user = User.objects.create()
    TodoItem.objects.create(text=request.POST['item_text'],user=new_user)
    return redirect(f'/todo/{new_user.id}/')

def show_items_for_a_user(request,id):
    user = User.objects.get(id=id)
    mytodoitems = TodoItem.objects.filter(user=user)
    return render(request, 'list.html', {'todo_items': mytodoitems})

#show all todo items for an user
def show_all_todo_item(request):
    if request.method == 'POST':
        TodoItem.objects.create(text=request.POST['item_text'])
    return render(request, 'list.html', {'todo_items': TodoItem.objects.all()})

def home_page(request):
    return render(request,'home.html')