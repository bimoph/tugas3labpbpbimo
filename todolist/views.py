from multiprocessing import context
from turtle import title
from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from todolist.forms import TaskForm

# @login_required(login_url='/todolist/login/')
# def show(request):
#     data_todolist = Task.objects.filter(user=request.user)

#     if request.method == 'POST':
#         temp = Task(user=request.user, 
#                     title=request.POST.get('todo'), 
#                     description=request.POST.get('description')
#                     )
#         temp.save()
#         return JsonResponse({'message': 'success'})

#     context = {
#         'list_todo': data_todolist,
#         'nama': request.user.username,
#         }
#     return render(request, "todolist.html", context)

# @login_required(login_url='/todolist/login/')
# def show_todolist(request):
#     data_task = Task.objects.filter(user=request.user) 
#     context = {
#         'list_task': data_task,
#         'last_login': request.COOKIES['last_login'],
#     }
#     return render(request, "todolist.html", context)
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {}
    return render(request, "todolist.html", context)

def add_todolist_item(request):
    if request.method == 'POST':
        
        # user = request.user
        # title = request.POST.get("harga_barang")
        # deskripsi = request.POST.get("deskripsi")

        new_task = Task(user=request.user, 
                    title=request.POST.get('title'), 
                    deskripsi=request.POST.get('description')
                    )
        new_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def show_json(request):
    item = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item))

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist")
            ) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('todolist:show_todolist')

    context = {'form': form}
    return render(request, 'create-task.html', context)