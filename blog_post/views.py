from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from user_account .models import *
from django.contrib import messages

# Create your views here.


def Home(request):
  posts = Post.objects.all().order_by('-created')
  paginator =  Paginator(posts,6)
  page_number = request.GET.get('page')
  posts = paginator.get_page(page_number)
 
  context = {
    'posts':posts,
   
  }
  
  return render(request,'post/index.html',context)



def blog_category(request, category):
  posts = Post.objects.filter(
    categories__name__contains=category
  ).order_by('-created')
  context = {
    'category':category,
    'posts':posts
  }
  
  return render(request,'post/blog_category.html',context)




def blog_detail(request, id):
  post = Post.objects.get(id=id)
  
  form = CommentForm()
  if request.method == 'POST':
    form = CommentForm(request.POST)
  if form.is_valid():
    body = request.POST.get('body')
    reply_id = request.POST.get('comment_id')
    comment_qs = None 
    if reply_id:
      comment_qs = Comment.objects.get(id=reply_id)
    comment = Comment.objects.create(post=post,body=body,author=request.user,reply=comment_qs)
    comment.save()
    messages.success(request,'comment added !!!!!')
    return HttpResponseRedirect(reverse('blog_post:blog_detail', args=[post.id]))
  comments = Comment.objects.filter(post=post,reply=None)
  context = {
    'post':post,
    'comments':comments,
    'form':form,
   
  }
  return render(request,'post/blog_detail.html',context)



def Search(request):
  posts = Post.objects.all()
  query = request.GET.get('q')
  if query:
    posts = Post.objects.all().filter(
      Q(title__icontains=query)|
      Q(body__icontains=query)
      
    )
    
  content = {'posts':posts}
  return render(request,'post/search.html',content)