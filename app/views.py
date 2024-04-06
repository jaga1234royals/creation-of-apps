from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mahi(request):
    return HttpResponse('<h1>He is named as cool captain for india</h1>')

def rahul(request):
    return HttpResponse('<h1><marquee>he is a captain of lucknow super gaints</marquee></h1>')

def jaddu(request):
    return HttpResponse('<h3><i>He is famous all rounder in india</i></h3>')
