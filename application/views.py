from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth, Permission
from django.contrib.sessions.models import Session
from django.http import JsonResponse,HttpResponse
from datetime import date
import json
# from .models import task_tbl
from django.views.decorators.csrf import csrf_exempt


def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
