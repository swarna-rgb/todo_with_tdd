from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import TodoItem
# Create your views here.


def home_page(request):
    # todo_item = TodoItem()
    # todo_item.text = request.POST.get('item_text', '')
    # todo_item.save()
    if request.method == 'POST':
       TodoItem.objects.create(text = request.POST.get('item_text','') )

       return  redirect('home_page')

    return render(request,'home.html',{'todo_items': TodoItem.objects.all()})