from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):
   return render(request,"index.html")


def logout(request):
   auth.logout(request)
   return redirect('/')