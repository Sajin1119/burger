from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User




def handleSignup(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        fphonenum = request.POST.get('phonenum')
        femail = request.POST.get('email')
        fpass1 = request.POST.get('pass1')
        fpass2 = request.POST.get('pass2')
        
        if fpass1 != fpass2:
            messages.error(request, "Passwords must be same")
        else:
            try:
                if User.objects.filter(username=fname).exists():
                    messages.error(request, "Email already exists")
                    return redirect('/auth/login')
            except User.DoesNotExist:
                pass  
            try:
                if User.objects.filter(email=femail).exists():
                    messages.error(request, "Email already exists")
                    return redirect('/auth/login')
            except User.DoesNotExist:
                pass  
            myuser=User.objects.create_user(femail,femail,fpass1)
            myuser.save()
            messages.info(request, "User created successfully")


    return render(request, "signup.html")

def handleLogin(request):
    if request.method == "POST":
        femail = request.POST['email']
        fpass1 = request.POST['pass1']

        # Authenticate the user
        myuser = authenticate(username=femail, password=fpass1)

        if myuser is not None:
            # Login the user if authentication is successful
            login(request, myuser)
            messages.info(request, "Logged in successfully")
            return redirect("/")
        else:
            # Authentication failed, show an error message
            messages.error(request, "Authentication failed. Please check your email and password.")

    return render(request, "login.html")





def handleLogout(request):
    logout(request)
    messages.error(request, "Logout successfull")
    return render(request,"login.html")
