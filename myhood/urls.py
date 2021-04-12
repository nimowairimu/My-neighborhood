from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = "myhood"

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/',views.register, name='registration'),
    path('all-hoods/', views.add_hood, name='hood'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/edit/', views.edit_profile, name='update-profile'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('exit_hood/<id>', views.exit_hood, name='exit-hood'),
    # path('api/hood/', views.HoodList.as_view()),
    # path('api/view_hood/', views.ViewHoodList.as_view()),
    path('search/', views.search_business, name='search'),
   
]