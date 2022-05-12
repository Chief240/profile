from re import search
from typing import Text
from django.shortcuts import redirect, render
from django.shortcuts import render
from .models import Trackin,Message,Subscribe
from .forms import ContactForm,SubscribeEmail
from django.contrib import messages

# Create your views here.
def myindex(request):
    if request.method == 'POST':
        search = request.GET.get('search')
        trackin = Trackin.objects.all().filter(Tracking_ID=search)
    return render(request, 'index/index.html', {'trackin': trackin})

def myindex(request):
    if request.method=="POST":
        form = SubscribeEmail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' You Have Successfully Subscribe To Our Services')
    else:
        form = SubscribeEmail
    return render(request, 'index/index.html')

def myabout(request):
    if request.method=="POST":
        form = SubscribeEmail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' You Have Successfully Subscribe To Our Services')
    else:
        form = SubscribeEmail
    return render(request, 'about/about.html')

def mycontact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Message was sent successfully, you will recieve a response via email within 24hours')
    else:
        form = ContactForm
    return render(request, 'account/contact.html')

def mycontact(request):
    if request.method=="POST":
        form = SubscribeEmail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' You Have Successfully Subscribe To Our Services')
    else:
        form = SubscribeEmail
    return render(request, 'account/contact.html')

def myservices(request):
    if request.method=="POST":
        form = SubscribeEmail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' You Have Successfully Subscribe To Our Services')
    else:
        form = SubscribeEmail
    return render(request, 'account/services.html')

def mytrack(request):
    if request.method=="POST":
        form = SubscribeEmail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' You Have Successfully Subscribe To Our Services')
    else:
        form = SubscribeEmail
    return render(request, 'account/track.html')

def searchbar(request):
    return render(request, 'account/searchbar.html',)