from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required
def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            BlogPost.objects.create(title=title, content=content)
            messages.success(request, 'Blog created successfully!')
            return redirect('blog_list')
        else:
            messages.error(request, 'All fields are required.')
    return render(request, 'main/blog_form.html')

@login_required
def blog_list_create(request):
    query = request.GET.get('q')
    blogs = BlogPost.objects.all().order_by('-created_at')
    if query:
        blogs = blogs.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            BlogPost.objects.create(title=title, content=content)
            messages.success(request, 'Blog created successfully!')
            return redirect('blog_list')
        else:
            messages.error(request, 'Both fields are required.')

    return render(request, 'main/blog_list.html', {'blogs': blogs, 'query': query})

@login_required
def blog_edit(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.save()
        messages.success(request, 'Blog updated!')
        return redirect('blog_list')

    return render(request, 'main/blog_edit.html', {'blog': blog})

@login_required
def blog_delete(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog deleted!')
        return redirect('blog_list')
    return render(request, 'main/confirm_delete.html', {'blog': blog})


    # We no longer need a separate confirmation page
    return redirect('blog_list')

@login_required
def blog_list(request):
    blog_list = BlogPost.objects.all()
    query = request.GET.get('q')
    if query:
        blog_list = blog_list.filter(title__icontains=query)
    
    paginator = Paginator(blog_list, 5)  # 5 blogs per page
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    
    return render(request, 'blog_list.html', {'blogs': blogs, 'query': query})


    # Blog creation logic
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            BlogPost.objects.create(title=title, content=content)
            messages.success(request, 'Blog created successfully!')
            return redirect('blog_list')
        else:
            messages.error(request, 'Both fields are required.')

    return render(request, 'main/blog_list.html', {
        'blogs': blogs,
        'query': query
    })
@login_required
def my_blogs(request):
    query = request.GET.get('q', '')
    # Only fetch blogs created by the logged-in user
    blogs = BlogPost.objects.filter(author=request.user)
    if query:
        blogs = blogs.filter(title__icontains=query)
    return render(request, 'main/my_blogs.html', {'blogs': blogs})