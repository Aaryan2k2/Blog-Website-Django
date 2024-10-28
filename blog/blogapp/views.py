from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .forms import PostCreate
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    posts=Post.objects.all().order_by('-date_posted')
    paginator=Paginator(posts,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,"blog/home.html",{"page_obj":page_obj}) 
     
      #Check paginator for function based views  

#class based view for home page

#Read Blog
'''
class PostListViews(ListView):
    model=Post
    template_name="blog/home.html"
    context_object_name="posts"
    ordering=['-date_posted']
    paginate_by=4 '''

#Blogs by specific user
def user_posts(request,username):
    user=get_object_or_404(User,username=username)
    posts=Post.objects.filter(author=user)
    
    paginator=Paginator(posts,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,"blog/user_posts.html",{"page_obj":page_obj,"user":user})

def about(request):
    return render(request,"blog/about.html")

def PostDetailView(request,blog_id):    
    blog=get_object_or_404(Post,id=blog_id)
    comments=Comment.objects.filter(post=blog)
    return render(request,"blog/post_detail.html",{'blog':blog,'comments':comments})

#Create Blog
@login_required
def post_create(request):
    if request.method=='POST':
        form=PostCreate(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            return redirect('blog-detail',blog_id=blog.id)
    else:
        form=PostCreate()
    return render(request,"blog/post_create.html",{'form':form}) 

#Edit Blog
@login_required
def post_edit(request,blog_id):
        edit_blog=get_object_or_404(Post,id=blog_id,author=request.user)
        if request.method=='POST':
            form=PostCreate(request.POST,instance=edit_blog)
            if form.is_valid():
                blog=form.save(commit=False)
                blog.author=request.user
                blog.save()
                return redirect('blog-detail',blog_id=blog.id)
        else:
            form=PostCreate(instance=edit_blog)
        return render(request,"blog/post_create.html",{'form':form})

#Delete Blog
@login_required
def post_delete(request,blog_id):
    delete_blog=get_object_or_404(Post,id=blog_id,author=request.user)
    if request.method=='POST':
        delete_blog.delete()
        messages.success( request,f'Your Blog has been deleted!')
        return redirect('blog-home')
    else:
        return render(request,"blog/post_delete.html")
    
@login_required    
def comments(request,blog_id):
    comment=request.POST.get('comment')
    post=get_object_or_404(Post,id=blog_id)
    if comment:
        comments=Comment(
            post=post,
            author=request.user,
            content=comment
        )
        comments=comments.save()
    return redirect("blog-detail",blog_id=blog_id)

@login_required
def comment_delete(request,comment_id):
    comment=get_object_or_404(Comment,id=comment_id)
    blog=comment.post
    comment.delete()
    return redirect('blog-detail',blog_id=blog.id)