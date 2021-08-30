from django.urls import path
from . import views 

app_name = 'user_account'

urlpatterns = [
   path('',views.Registration,name="register"),
   path('login/',views.Login,name='login'),
   path('logout/',views.UserLogout,name='logout'),
   path('profile_edit/',views.EditProfile,name='profile_edit'),
]
