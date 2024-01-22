from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def read_more(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/read_more.html', {'post': post})

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.error(request, "It is not your post, and you cannot edit it.")
        return redirect('blog:post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('blog:post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/update_post.html', {'form': form, 'post': post})
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.error(request, 'You cannot delete this post as it does not belong to you.')
        return redirect('blog:post_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted successfully!')
        return redirect('blog:post_list')

    return render(request, 'blog/delete_post.html', {'post': post})