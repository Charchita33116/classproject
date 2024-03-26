from django.urls import path
from .views import *

urlpatterns = [
    path("hello/",hello1),
    path('hello1/',hello,name='hello'),
    path("",newhomepage,name='newhomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('ran1/',random1,name='random1'),
    path('ran/',random123,name='random123'),
    path('date1/',getdate1,name='getdate1'),
    path('date/',get_date,name='get_date'),
    path('tzfunctionall/',tzfunctioncall,name='pytzexample'),
    path('reg/',registerlogin1,name='registerlogin1'),
    path('register/',registerlogin,name='registerlogin'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('login1/', login1, name='login1'),
    path('signup1/', signup1, name='signup1'),
    path('logout/', logout, name='logout'),
    path('contact1/', contactmail1, name='conactmail1'),
    path('contact/',contactmail, name='contactmail'),
    path('weather/',weatherlogic, name='weather'),
    path('weathercall/', weathercall, name='weathercall'),

]