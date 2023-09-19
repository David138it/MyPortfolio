from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from .forms import *
from .models import *
from .utils import *
from django.views.generic import ListView, DetailView, CreateView, FormView
class ProgressHome(DataMixin, ListView):
	model=Progress
	template_name='progress/index.html'
	context_object_name='posts'
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		c_def = self.get_user_context(title="Главная страница")
		return dict(list(context.items())+list(c_def.items()))
	def get_queryset(self):
		return Progress.objects.filter(is_published=True).select_related('cat')
def about(request):
	contact_list=Progress.objects.all()
	paginator=Paginator(contact_list,2)
	page_number=request.GET.get('page')
	page_obj=paginator.get_page(page_number)
	return render(request, 'progress/about.html', {'page_obj':page_obj, 'menu':menu, 'title':'Обо мне'})
def pageNotFound(request, exception):
	return HttpResponseNotFound("<h1>Страница не найдена</h1>")	
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
	form_class=AddPostForm
	template_name='progress/addpage.html'
	success_url=reverse_lazy('home')
	login_url = reverse_lazy('home')
	raise_exception = True
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		c_def = self.get_user_context(title="Добавление статьи")
		return dict(list(context.items())+list(c_def.items()))
#def contact(request):
#	return HttpResponse("Обратная связь")
class ShowPost(DataMixin, DetailView):
	model=Progress
	template_name='progress/post.html'
	slug_url_kwarg='post_slug'
	context_object_name='post'
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		c_def = self.get_user_context(title=context['post'])
		return dict(list(context.items())+list(c_def.items()))
class ProgressCategory(DataMixin, ListView):
	model=Progress
	template_name='progress/index.html'
	context_object_name='posts'
	allow_empty=False
	def get_queryset(self):
		return Progress.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		c = Category.objects.get(slug=self.kwargs['cat_slug'])
		c_def = self.get_user_context(title='Категория - ' + str(c.name), cat_selected=c.pk)
		return dict(list(context.items())+list(c_def.items()))
class RegisterUser(DataMixin, CreateView):
	form_class=UserCreationForm
	template_name='progress/register.html'
	success_url=reverse_lazy('login')
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		c_def=self.get_user_context(title="Регистрация")
		return dict(list(context.items())+list(c_def.items()))
	def form_valid(self, form):
		user=form.save()
		login(self.request, user)
		return redirect('home')
class LoginUser(DataMixin, LoginView):
	form_class=AuthenticationForm
	template_name='progress/login.html'
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		c_def=self.get_user_context(title="Авторизация")
		return dict(list(context.items())+list(c_def.items()))
	def get_success_url(self):
		return reverse_lazy('home')	
def logout_user(request):
	logout(request)
	return redirect('login')
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'progress/contact.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')