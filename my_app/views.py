from django.shortcuts import render
from .models import User, Computer, Order
from django.http import HttpResponse

# Create your views here.

def index(request):
    computers = Computer.objects.all()
    return render(request, "index.html", {'computers': computers})

def indexx(request):
    orders = Order.objects.all()
    return render(request, "indexx.html", {'orders': orders})

def indexxx(request):
    users = User.objects.all()
    return render(request, "indexxx.html", {'users': users})

def post(request, id):
    computer = Computer.objects.get(id=id)
    orders = Order.objects.select_related('user').filter(computer=computer)
    return render(request, "post.html", {'computer': computer, 'orders': orders})