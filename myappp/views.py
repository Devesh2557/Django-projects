from django.shortcuts import render,HttpResponse,redirect
from .models import Contact,Blog
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def index(request):
    blog_data = Blog.objects.all()
    context = {
        'Blog':blog_data
    }    
    return render(request,'rightside.html',context)

def about(request):
    
    return render(request,'about.html')

def post(request,id):
    post_data = Blog.objects.filter(id=id)
    context = {
        'main':post_data[0]
    }
    return render(request,'post.html',context)

def contact(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        Subject = request.POST['Subject']
        Message = request.POST['Message']
        Contact(Name=Name,Email=Email,Subject=Subject,Message=Message).save()
        return HttpResponse("Data Save Successfully")
    return render(request,'contact.html')



def postblog(request):
    if request.method == "POST":
        image = request.POST['image']
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        Blog(image=image,title=title,description=description,date=date).save()
        return HttpResponse("Post Saved Successfully")
    return render(request,'postblog.html')


def signuphandle(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = User(username=name,email=email)
        if(password==confirm_password):
            user.set_password(password)
            user.save()
            messages.success(request,"Your Account Successfully Created")
        else:
            messages.success(request,"Boths field should be same")
    return render(request,'signup.html')


def loginhandle(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name,password=password)  
        
        if user is not None:
            login(request,user)
            return redirect("/")
        
        else:
            messages.success(request,"user not found..")
    return render(request,'login.html')   


def logouthandle(request):
    logout(request)    
    return redirect('/login/') 
    
            



    

    