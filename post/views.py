from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

from django.forms import ModelForm

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body']

def index(request):

    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts})    

def get_post(request, pk):

    post = Post.objects.get(pk=pk)

    return render(request, 'view_post.html', {'post': post})

def create_post_form(request):
    
    if request.method == POST:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

def update_post(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':

        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PostForm(instance=post)
    
    return render(request, 'update_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == POST:
        post.delete()
        return redirect(home)
    return render(request, 'comfirm_post_delete.html', {'post' : post})