from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *
menu=[{'title':"О сайте", 'url_name':'about'}, 
	{'title':"Добавить статью", 'url_name':'add_page'},
	{'title':"Обратная связь", 'url_name':'contact'},
	{'title':"Войти", 'url_name':'login'}]
class ProgressHome(ListView):
	model=Progress
	template_name='progress/index.html'
	context_object_name='posts'
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		context['menu']=menu
		context['title']='Главная страница'
		context['cat_selected']=0
		return context
	def get_queryset(self):
		return Progress.objects.filter(is_published=True)
def about(request):
	return render(request, 'progress/about.html', {'menu':menu, 'title':'О сайте'})
def pageNotFound(request, exception):
	return HttpResponseNotFound("<h1>Страница не найдена</h1>")	
class AddPage(CreateView):
	form_class=AddPostForm
	template_name='progress/addpage.html'
	success_url=reverse_lazy('home')
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		context['title']='Добав статьи'
		context['menu']=menu
		return context
def contact(request):
	return HttpResponse("Обратная связь")
def login(request):
	return HttpResponse("Авторизация")
class ShowPost(DetailView):
	model=Progress
	template_name='progress/post.html'
	slug_url_kwarg='post_slug'
	context_object_name='post'
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		context['title']=context['post']
		context['menu']=menu
		return context
class ProgressCategory(ListView):
	model=Progress
	template_name='progress/index.html'
	context_object_name='posts'
	allow_empty=False
	def get_queryset(self):
		return Progress.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data(**kwargs)
		context['title']='Категория - ' + str(context['posts'][0].cat)
		context['menu']=menu
		context['cat_selected']=context['posts'][0].cat_id
		return context