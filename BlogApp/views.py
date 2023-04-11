from django.shortcuts import render , redirect

from . models import BlogModel 
from . forms import BlogForm

from django.contrib import messages
# Create your views here.

def home_view(request):
    
    blogs = BlogModel.objects.all()
    
    # print(blogs)

    context = {"blogs" : blogs}

    return render(request , "home.html" , context) 


def dashboard_view(request):

    blogs = BlogModel.objects.all()
    
    # print(blogs)

    context = {"blogs" : blogs}

    return render(request , "dashboard.html" , context)

def addblog_view(request):

    forms = BlogForm()
    if request.method == "POST":
        forms = BlogForm(request.POST)
        if forms.is_valid():
            forms.save()

            messages.info(request , "Blog Added")

        return redirect('dashboard')

    context = {"forms" : forms}
    
    return render(request , "addblog.html" , context)

def deleteblog_view(request , id):

    blog = BlogModel.objects.get(id = id)
    # print(blog)
    blog.delete()
    messages.info(request , "Successfully Blog Deleted")

    return redirect("dashboard")


def updateblog_view(request , id):

    blog = BlogModel.objects.get(id = id)
    if request.method == "POST":

        new_title = request.POST.get('Updatetitle')
        new_desc = request.POST.get('updatedesc')
    
        blog.title = new_title
        blog.desc = new_desc
        blog.save()
        messages.success(request , 'Successfully Blog Updated')

        return redirect('dashboard')

    context = {"blog" : blog}

    return render(request , 'updateblog.html' , context)

