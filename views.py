from http.client import HTTPResponse
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
#from .models import adminLogin
from .decorations import allowed_users

#@admin_only
def home(request):
    return render(request, 'home.html')

@allowed_users(allowed_roles=['admin'])
def adminPage(request):
    return render(request, 'templates/adminPage')
    #template = loader.get_template('home.html')
    #return HttpResponse(template.render({}, request))
