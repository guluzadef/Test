from django.shortcuts import render
from django.views import generic
from default.models import *
from .forms import AddFood
# Create your views here.

def Home(request):
    context={}
    context["sitename"]=Site_name.objects.all()
    context['menu']=Menu.objects.all()
    context['main']=Main.objects.all()
    context['first']=First.objects.last()
    context['second']=Second.objects.last()
    context['meals']=Meals.objects.all()
    context['footer']=Footer.objects.all()


    return render(request,"index.html",context)


def add_food(request):
    context={}
    context["form"]=AddFood()
    return render(request,"yemek.html",context)