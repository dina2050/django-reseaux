from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import TemplateView
from .models import Profil, User
from .forms import ProfilFormSet, SearchForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from dal import autocomplete
from django.utils.html import format_html
from django import forms
from django.contrib.gis.measure import D
# Create your views here.
    

class HomePageView(TemplateView):
    template_name = "blog/homepage.html"

class ProfilListView(ListView):
    model=Profil
    # queryset = Profil.objects.all()
    # def get_queryset(self):
    #     query = self.request.GET.get('q',None)
    #     if query == None:
    #         object_list = Profil.objects.all()
    #     else:
    #         object_list = Profil.objects.filter(
    #             Q (user__username__icontains = query) |
    #             Q (user__first_name__icontains = query) |
    #             Q (user__last_name__icontains = query) 
    #         )
    #     return object_list
    def get_context_data(self,**kwargs):
            context = ListView.get_context_data(self,**kwargs)
            context['search_form'] = SearchForm()
            print(vars(context['object_list'][0]))
            return context
class ProfilAutocomplete(autocomplete.Select2QuerySetView):
    model=Profil
    queryset = Profil.objects.all()
    def get_queryset(self):
        query = self.request.GET.get('q',None)
        if query == None:
            object_list = Profil.objects.all()
        else:
            object_list = Profil.objects.filter(
                Q (user__username__icontains = query) |
                Q (user__first_name__icontains = query) |
                Q (user__last_name__icontains = query) 
            )
        return object_list

    def get_result_label(self,item):
        return format_html('<a href="{}">{}', item.user.username, item.user.username)


class ProfilDetailView(DetailView):
    model=Profil
    slug_field = "user__username"
    slug_url_kwarg = "username"

    def get_context_data(self,**kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        current_profile = self.request.user.profil
        context['reco_list'] = Profil.objects.filter(geom__distance_lte=(current_profile.geom, D(km=100)))        
        
        return context

class ProfilCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "blog/profil_form.html"


    def get_context_data(self,**kwargs):
        context = CreateView.get_context_data(self,**kwargs)
        context['profil_form'] = ProfilFormSet()
        return context
    
    def form_valid(self,form):
        if form.is_valid():
            self.new_user = form.save(commit=False) #doesn't save info but has created a new user
            profil_form = ProfilFormSet (self.request.POST, instance = self.new_user)
            if profil_form.is_valid():
                form.save()
                profil_form.save()
           

                # username = self.request.POST['username']
                # password = self.request.POST['password1']
                user = authenticate(self.request, username=username, password=password)
                login(self.request, self.new_user)
                return HttpResponseRedirect(self.get_success_url())


        context = {
            'form' : form,
            'profil_form' : profil_form
        }
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy("profile_detail", args=[self.new_user.username])


class ProfilUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "blog/profil_form.html"


    def get_context_data(self,**kwargs):
        context=UpdateView.get_context_data(self,**kwargs)
        context['profil_form'] = ProfilFormSet(instance=self.get_object())
        return context
    
    def form_valid(self,form):
        profil_form = ProfilFormSet (self.request.POST, instance = self.get_object())
        if profil_form.is_valid() and form.is_valid():
            profil_form.save()
            form.save()
            return HttpResponseRedirect(self.get_success_url())

        else:
            context = {
                'form' : form,
                'profil_form' : profil_form
            }
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy("profile_detail", args=[self.get_object().username])


class ProfilDeleteView(DeleteView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "blog/user_confirm_delete.html"
    def get_success_url(self):        
        return reverse_lazy('homepage')


class FollowView(View):


    def get(self, request, *args, **kwargs):
        current_username = kwargs["username"]
        friend_username = kwargs["friend_username"]

        current_profile = Profil.objects.get(user__username=current_username) 
        friend_profile = Profil.objects.get(user__username=friend_username) 

        current_profile.follows.add(friend_profile)

        return HttpResponseRedirect(reverse_lazy("profile_list"))


class UnFollowView(View):


    def get(self, request, *args, **kwargs):
        current_username = kwargs["username"]
        friend_username = kwargs["friend_username"]

        current_profile = Profil.objects.get(user__username=current_username) 
        friend_profile = Profil.objects.get(user__username=friend_username) 

        current_profile.follows.remove(friend_profile)

        return HttpResponseRedirect(reverse_lazy("profile_list"))


class ProfilMapView(ListView):
    model = Profil
    template_name = "blog/map.html"

