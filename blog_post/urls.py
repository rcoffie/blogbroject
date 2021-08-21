from django.urls import path
from . import views 

app_name = 'blog_post'

urlpatterns = [
   path('',views.Home,name='home'),
   path('detail/<int:id>/',views.blog_detail,name='blog_detail'),
   path('<category>/',views.blog_category,name="blog_category")
]
