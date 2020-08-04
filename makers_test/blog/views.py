from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from .models import Category, Post
from .forms import AddPostForm, UpdatePostForm


def categories_list(request):
    categories = Category.objects.all()
    return render(request,
                  'blog/index.html',
                  {'categories_list': categories})


def posts_list(request):
    category = request.GET.get('category')
    posts = Post.objects.filter(category_id=category)
    return render(request, 'blog/posts_list.html', {'posts': posts})


def post_details(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/post_details.html', {'post': post})


def add_post(request):
    if request.POST:
        post_form = AddPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save()
            return redirect(post.get_absolute_url())

    else:
        post_form = AddPostForm()
    return render(request, 'blog/add_post.html', {'post_form': post_form})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_form = UpdatePostForm(request.POST, request.FILES or None, instance=post)
    if post_form.is_valid():
        post_form.save()
        return redirect(post.get_absolute_url())
    return render(request, 'blog/update_post.html', {'post_form': post_form, 'post': post})


def delete_post(request, pk):
    return render(request, 'blog/delete_post.html', {})
