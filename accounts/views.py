from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth




# from . models import register


# Create your views here.
def register(request):

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,contact=contact,address=address,city=city,state=state,pincode=pincode,password=password1  )
        user.save()
        print("user created")
        return redirect ('/')  

    else:
        return render (request,'register.html')

    