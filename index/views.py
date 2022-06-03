from re import search
from typing import Text
from django.shortcuts import redirect, render
from django.shortcuts import render
from .models import Trackin,Message,Subscribe
from .forms import ContactForm,SubscribeEmail
from django.contrib import messages
import string
import random

# Create your views here.
def myindex(request):
    qs = []
    if request.method == 'POST':
        track_id = request.POST.get('id')
        fillid = Trackin.objects.filter(Tracking_ID=track_id)
        if fillid.exists():
            qs = Trackin.objects.get(Tracking_ID=track_id)
            context = {'data':qs}
            return render(request,'account/faq.html',context)
        else:
            messages.error(request, 'Invalid Tracking ID')

        form = SubscribeEmail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' You Have Successfully Subscribe To Our Services')
        else:
            form = SubscribeEmail
    else:
        return render(request, 'index/index.html')
    return render(request, 'index/index.html')

# def myindex(request):
#     if request.method=="POST":
#         form = SubscribeEmail(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, ' You Have Successfully Subscribe To Our Services')
#     else:
#         form = SubscribeEmail
#     return render(request, 'index/index.html')

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
    qs = []
    if request.method == 'POST':
        track_id = request.POST.get('id')
        fillid = Trackin.objects.filter(Tracking_ID=track_id)
        if fillid.exists():
            qs = Trackin.objects.get(Tracking_ID=track_id)
            context = {'data':qs}
            return render(request,'account/faq.html',context)
        else:
            messages.error(request, 'invalid ID')

        form = SubscribeEmail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' You Have Successfully Subscribe To Our Services')
        else:
            form = SubscribeEmail
    else:
        return render(request, 'account/track.html')
    return render(request, 'account/track.html')
