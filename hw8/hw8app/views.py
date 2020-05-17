from django.shortcuts import render, redirect
from .models import Post
import time

# Create your views here.
def index(request):
    movie=Post.objects.filter(category='movie')
    movie_num=movie.count()
    drama=Post.objects.filter(category='drama')
    drama_num=drama.count()
    entertain=Post.objects.filter(category='entertain')
    entertain_num=entertain.count()
    
    return render(request,'index.html', { 'movie':movie_num,'drama':drama_num,'entertain':entertain_num })

def new(request):
    if request.method == "POST" :
        # print(request.POST)
        new_post = Post.objects.create(
            category = request.POST['category'],
            title = request.POST['title'],
            content = request.POST['content'], 
         )
        return redirect(detail, Post_pk=new_post.pk)
    else:
        return render(request, 'new.html')

def movie(request):
    movies=Post.objects.filter(category='movie')
    return render(request,'movie.html',{'movies':movies})

def drama(request):
    dramas=Post.objects.filter(category='drama')
    return render(request,'drama.html',{'dramas':dramas})

def entertain(request):
    entertains=Post.objects.filter(category='entertain')
    return render(request,'entertain.html',{'entertains':entertains})

def detail(request, Post_pk):
    post = Post.objects.get(pk=Post_pk)
    return render(request,'detail.html',{'post':post})

