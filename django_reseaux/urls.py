"""django_reseaux URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import ProfilListView, ProfilDetailView, ProfilUpdateView, HomePageView, ProfilCreateView, ProfilDeleteView, FollowView, UnFollowView, ProfilAutocomplete, ProfilMapView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("profiles", ProfilListView.as_view(), name="profile_list"),
    path("profiles/<str:username>/", ProfilDetailView.as_view(), name="profile_detail"),
    path("profiles/<str:username>/edit/", ProfilUpdateView.as_view(), name="profil_update"),
    path("",HomePageView.as_view(),name="homepage"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("profile/create/",ProfilCreateView.as_view(),name="profil_create"),
    path('profile/<str:username>/delete', ProfilDeleteView.as_view(), name='delete'),
    path('profile/<str:username>/follow/<str:friend_username>', FollowView.as_view(), name='follow'),
    path('profile/<str:username>/unfollow/<str:friend_username>', UnFollowView.as_view(), name='unfollow'),
    
    path(r'^profil-autocomplete/$', ProfilAutocomplete.as_view(), name='profil-autocomplete',),
    path("map/",ProfilMapView.as_view(), name="map"),
    
    # path('profile/messages/', include('postman.urls', namespace='postman')),
   
]
