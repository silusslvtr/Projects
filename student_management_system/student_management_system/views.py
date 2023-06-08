from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'index.html')

def kungfustyles(request):
    return render(request, 'kungfustyles.html')

def login(request):
    return render(request, 'login.html')

def shaolin(request):
    return render(request, 'shaolin.html')

def taichi(request):
    return render(request, 'taichi.html')

def qigong(request):
    return render(request, 'qigong.html')

def sanda(request):
    return render(request, 'sanda.html')