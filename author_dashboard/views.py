from django.shortcuts import render,redirect, HttpResponse
from blog_post import *
from .forms import *
from user_account .models import *
from django.views import generic
from django.views.generic import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.



class CreatePost(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'author_dashboard/create_post.html'
  success_url = reverse_lazy('blog_post:home')
  
  def form_valid(self, form):
      form.instance.created_by = self.request.user
      return super().form_valid(form)
  
  

class EditPost(UpdateView):
  model = Post
  form_class = PostForm
  # fields  = '__all__'
  template_name = 'author_dashboard/update_post.html'
  template_url = reverse_lazy('author_dashboard:home')
  success_url  = reverse_lazy('author_dashboard:home')
  
  

def Home(request):
  
  posts = Post.objects.all()
  context = {'posts':posts}
  
  return render(request,'author_dashboard/home.html',context)



def DeletePost(request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return redirect('author_dashboard:home')