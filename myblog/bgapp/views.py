from django.http import HttpResponse,request
from django.shortcuts import render
from .models import Post

# Create your views here.
# views handles the request and returns a response
def post_list(request):
    queryset= Post.objects.all()

    context={
        "object_list":queryset,

        "title":"List"
    }
    return render(request,'index.html',context)


def post_create(request):
    context={
        "title":"create"
    }
    return render(request,'index.html',context)

def post_detail(request): # retrieve
    return HttpResponse("<h1>Detail</h1>")

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
