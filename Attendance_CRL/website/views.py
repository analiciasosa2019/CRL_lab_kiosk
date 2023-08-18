from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    templater = loader.get_template("index.html")
    context = {
        "latest_question_list": 5,
    }
    return HttpResponse(templater.render(context, request))

def attendance(request):
    templater = loader.get_template("attendance.html")
    context = {
        "latest_question_list": 5,
    }
    return HttpResponse(templater.render(context, request))

def projects(request):
    templater = loader.get_template("projects.html")
    context = {
        "latest_question_list": 5,
    }
    return HttpResponse(templater.render(context, request))

def information(request):
    templater = loader.get_template("information.html")
    context = {
        "latest_question_list": 5,
    }
    return HttpResponse(templater.render(context, request))