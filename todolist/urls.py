from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, show_json, add_todolist_item

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('create-task-ajax/', add_todolist_item, name='add_todolist_item'),
]