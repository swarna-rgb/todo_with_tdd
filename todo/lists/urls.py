from django.urls import path
from .views import home_page, show_all_todo_item,create_todo_item,show_items_for_a_user,add_items_for_a_user
urlpatterns = [
    path('todo/', home_page, name = 'home_page'),
    path('todo/showall/', show_all_todo_item),
    path('todo/<int:id>/', show_items_for_a_user),
    path('todo/<int:user_id>/additem/', add_items_for_a_user),
    path('todo/newtodoitem/', create_todo_item),
]