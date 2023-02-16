

from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf

from .forms import PersonCreationForm
from .models import Person, Branch
from django.contrib.auth.hashers import make_password
# Create your views here.

def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)

      if user is not None:
         auth.login(request, user)
         return render(request,'new.html')
      else:
         messages.info(request, "Invalid credentials")
         return redirect('login')

   return render(request, 'login.html')

def logout(request):
   auth.logout(request)
   return redirect('/')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request, "User already exist.Plz try another")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            elif User.objects.filter(username=None,email=None,password=None):
                messages.info(request,"Plz enter details")

            else:
                user = User.objects.create_user(username=username,
                                                email=email, password=password)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
            return redirect('register')

    return render(request,'register.html')

def form(request):
   return redirect('/')


def demo(request):
   return redirect('/')




def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'branches': branches})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def submit(request):
    # check if the request is post
    if request.method == 'POST':

        # Pass the form data to the form class
        details = PersonCreationForm(request.POST)

        # In the 'form' class the clean function
        # is defined, if all the data is correct
        # as per the clean function, it returns true
        if details.is_valid():

            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database
            post = details.save(commit=False)

            # Finally write the changes into database
            post.save()

            # redirect it to some another page indicating data
            # was inserted successfully
            return render(request,"message.html")

        else:

            # Redirect back to the same page if the data
            # was invalid
            return render(request, "home.html", {'form': details})
    else:

        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = PostForm(None)
        return render(request, 'home.html', {'form': form})

