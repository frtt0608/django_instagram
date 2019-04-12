from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, ImageForm
from .models import Post

# Create your views here.
def list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'posts/list.html', context)
    
    
def posts_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.FILES)
        if post_form.is_valid():
            post = post_form.save()
            files = request.FILES.getlist('file')
            for file in files:
                request.FILES['file'] = file
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect(post)
    else:
        post_form = PostForm()
        image_form = ImageForm()
    context = {'post_form':post_form, 'image_form':image_form}
    return render(request, 'posts/form.html', context)


def posts_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.hit += 1
    post.save()
    context = {'post':post}
    return render(request, 'posts/posts_detail.html', context)
    
    
def posts_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    return redirect('posts:list')
    
    
def posts_update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post=post_form.save()
            return redirect(post)
    else:
        post_form = PostForm(request.POST, instance=post)
    context = {'post_form':post_form}
    return render(request, 'posts/form.html', context)