from django.shortcuts import render
from blog.models import Post, Comment  
from blog.forms import CommentForm

def blogIndex(request):
    posts = Post.objects.all().order_by("-createdOn")
    context = {"posts": posts}
    return render(request, "blogIndex.html", context) 

def blogCategory(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-createdOn')
    context = {"category": category, "posts": posts}
    return render(request, "blogCategory.html", context) 

def blogDetail(request, id):
    post = Post.objects.get(pk=id)
    
    form = CommentForm() 
    if request.method == 'POST':
        form = CommentForm(request.POST) 
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            ),
            comment[0].save() 
            
    comments = Comment.objects.filter(post=post) 
    context = {
        "post": post, 
        "comments": comments,
        "form": form 
    } 
    return render(request, "blogDetail.html", context) 

