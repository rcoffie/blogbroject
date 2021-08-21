from django import forms 
from django.forms import ModelForm 
from blog_post .models import * 

class PostForm(ModelForm):
  
  categories = forms.ModelMultipleChoiceField(
    queryset = Category.objects.all(),
    widget= forms.CheckboxSelectMultiple
  )
 
  class Meta:
    model = Post
    fields = ['title','body','image','categories']
    
  
    
    
    