from contextlib import _RedirectStream
from django.shortcuts import redirect , render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
import os
import shared

#To open gdb. 
from pygdbmi.gdbcontroller import GdbController
#To use gdb commands and get gdb console outputs.
from pygdbmi import gdbmiparser
#To name log files.
from datetime import datetime
#To verify gdb console outputs.
import re
# To handle arguments to the script
import sys
#To start openocd session
import os
import time
import CombiledBOTH


# Create your views here.

def home(request):
    return render(request , "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        
        myuser = User.objects.create_user(username , email , pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()

        messages.success(request , "you account has been created")

        return redirect('signin')


    return render(request , "authentication/signup.html")


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
    
    #for passwprd matching
        user = authenticate(username =  username , password = pass1)

        if user is not None:
            login(request , user)
            fname = user.first_name
            print(fname)
            return render(request , "authentication/index.html" , {'fname' : fname })
        else:
            messages.error(request , "Wrong Credentials :)")
            return redirect('home')


    return render(request , "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request , "Logged out Successfully")
    return redirect(home)


def transmite(request):
    if request.method == "POST":
        data1 = request.POST['data1']
        data1 = '"' + data1 + '"'

        # commandRun = 'python allbaudrate.py' 
        # os.system(commandRun)

        # result = CombiledBOTH.functionOfsameMain9600("9600" )
        # print(result)

        result = CombiledBOTH.functionOfsameMain19200(data1)
        print(result)

        # result = CombiledBOTH.functionOfsameMain38400(data1 )
        # print(result)

        # result = CombiledBOTH.functionOfsameMain57600("57600" )
        # print(result)

        # result = CombiledBOTH.functionOfsameMain115200("115200" )
        # print(result)

        finalstring = ''

        finalstring = finalstring + 'Transmitted String : ' + result[0] + ','
        finalstring = finalstring + 'Received  String : ' + result[1]   + ','
        finalstring = finalstring + result[2]



        print(result)
        
        return render(request, "authentication/my_template.html", {"message": finalstring})

    else:
        return redirect(home)