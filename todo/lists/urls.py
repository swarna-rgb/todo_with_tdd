from django.urls import path
from .views import home_page
urlpatterns = [
    path('todo/', home_page, name = 'home_page')
]