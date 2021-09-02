from django.shortcuts import render,redirect, HttpResponse
from blog_post import *
from .forms import *
from user_account .models import *
from django.views import generic
from django.views.generic import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.


@method_decorator(login_required,name='dispatch')
class CreatePost(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'author_dashboard/create_post.html'
  success_url = reverse_lazy('blog_post:home')
  
  def form_valid(self, form):
      form.instance.created_by = self.request.user
      return super().form_valid(form)
  
  
@method_decorator(login_required,name='dispatch')
class EditPost(UpdateView):
  model = Post
  form_class = PostForm
  # fields  = '__all__'
  template_name = 'author_dashboard/update_post.html'
  template_url = reverse_lazy('author_dashboard:home')
  success_url  = reverse_lazy('author_dashboard:home')
  
  
@login_required
def Home(request):
  
  posts = Post.objects.all().filter(created_by =request.user)
  context = {'posts':posts}
  
  return render(request,'author_dashboard/home.html',context)



def DeletePost(request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return redirect('author_dashboard:home')


