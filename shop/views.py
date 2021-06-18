from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from  .models import item2,help



def about(request):
    return render(request,'aboutwork.html')
def help(request):
    return render(request,'help.html')
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return render(request, 'fhome.html')
        print("not login")

    else:
        product = item2.objects.all()

        print(product)
        parsms = {'item2': product}
        for i in product:
           print(i.id)

        return render(request,'mainhome.html',parsms)
        print("user is log in ")




def index22(request):
    djtext = request.POST.get('username', 'default')
    print(djtext)
    return HttpResponse(djtext)


def index2(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return HttpResponse("kaam ho gaya")

    else:
        return HttpResponse("404 - Not found")





def loginUser(request):

    if request.user.is_anonymous:
        print("alrady not login")

    else:
        print("user is log in already")



    if request.method=="POST":
        username = request.POST.get('loginusername')
        password = request.POST.get('pass')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            # this user have account
            login(request, user)
            print('''return redirect("/")''')
            return redirect("/")

        else:
            # No backend authenticated the credentials
            # this user have no account
            print('''return render(request, 'fhome.html')''')
            return render(request, 'fhome.html')


    return render(request, 'fhome.html')



def logoutUser(request):
    logout(request)
    return redirect("/")


def other(request):
    print(request.user)
    if request.user.is_anonymous:
        return render(request, 'fhome.html')
        print("not login")

    else:
        amazonlink= request.POST['amazonlink']
        parsms={'amazon':amazonlink}




        return render(request, 'other.html', parsms)
        print("user is log in ")
