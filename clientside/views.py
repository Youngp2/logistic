from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from adminside.models import Order
from django.contrib import messages
from .models import Client
from . forms import QuoteForm

# Create your views here.

def Home(request):
    return render(request, 'homepage.html')

def About(request):
    return render(request, 'about.html')

def Services(request):
    return render(request, 'services.html')

def Track(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        try:
            model_instance = Order.objects.get(tracking_number=tracking_number)
            return render(request, 'track_and_trace.html', {'model_instance': model_instance})
        except Order.DoesNotExist:
            messages.error(request, 'Order not found.')
    return render(request, 'track_and_trace.html')


def Contact(request):
    form = QuoteForm()
    if request.method =='POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ClientSide:contact')
    context = {'form':form}
    return render(request, 'contact.html',context )

def details(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'details.html', {'order': order})

def deleteorder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method =='POST':
        order.delete()
        return redirect('AdminSide:order-list')
    context = {'order': order}
    return render(request, 'delete.html', context)

def Quote(request):
    form = QuoteForm()
    if request.method =='POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ClientSide:get-a-quote')
    context = {'form':form }
    return render(request, 'get-a-quote.html')

