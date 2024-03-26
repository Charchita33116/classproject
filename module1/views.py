import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request,'hello.html')
def hello1(request):
    return HttpResponse("<center> <font color=blue><hr>Welcome to TTM Homepage</center>")

def newhomepage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method=="POST":
        user_input = request.POST['Charchita']
        print(f'User input: {user_input}')
    #return HttpResponse('Form submitted successfully')
        a1 = {'user_input': user_input}
        return render(request,'print_to_console.html',a1)

def random1(request):
    return render(request,'random123.html')

def random123(request):
    import string
    import random
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = int(input1)
    ran1 = ''.join(random.sample(string.digits,input2))
    print(ran1)
    a2 = {'ran1': ran1}
    return render(request,'random123.html',a2)

def getdate1(request):
    return render(request,'get_date.html')

import datetime
from django.shortcuts import render
from .forms import *
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return  render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
        return render(request,'get_date.html',{'form':form})

def tzfunctioncall(request):
    return render(request,'pytzexample.html')

def registerlogin1(request):
    return render(request,'registerlogin.html')

from .models import *
from django.shortcuts import render
def registerlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1 = "Email already registered.Choose a different email."
            return render(request,'myregisterpage.html',{'message1':message1})
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage.html')
    return render(request,'myregisterpage.html')


from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def signup1(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass2)
                user.save()
                messages.info(request,'Account created successfully')
                return render(request,'login.html')
        else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')

def contactmail1(request):
    return render(request,'contactus.html')
def contactmail(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment + '-------------------This is just the copy of '
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comment)
        data.save()
def weathercall(request):
    return render(request,'weatherappinput.html')


def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'c91aeb37d0e81e1b9ad0e70b321b3225'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})



