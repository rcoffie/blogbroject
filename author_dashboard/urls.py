from django.urls import path
from . import views 

app_name = 'author_dashboard'

urlpatterns = [
  path('create/',views.CreatePost.as_view(),name='create'),
  path('',views.Home,name="home"),
  path('update/<int:pk>/',views.EditPost.as_view(),name="update"),
  path('delete/<int:id>/',views.DeletePost,name="delete")
]
