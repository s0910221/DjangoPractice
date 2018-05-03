from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostModelForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {
        'posts': posts
    })


def show(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/show.html', {
        'post': post
    })


# def new(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         if title == '' or content == '':
#             return render(request, 'posts/new.html',{
#                 'error':['有欄位未填寫']
#             })

#         Post.objects.create(title=title, content=content)
#         return redirect('posts_index')
#     return render(request, 'posts/new.html')

def new(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('posts:index')
    return render(request, 'posts/new.html', {
        'form': form
    })


def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostModelForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:index')

    return render(request, 'posts/edit.html', {
        'form': form
    })


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts:index')
