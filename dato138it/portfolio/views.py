from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
menu=[{'title':"Добавить статью", 'url_name':'add_page'},
	{'title':"Feedback:", 'url_name':'contact'},
	{'title':"Войти", 'url_name':'login'}]
def index(request):
	posts=Portfolio.objects.all()
	context={'posts':posts, 
		'menu':menu, 
		'title':'Главная страница',
		'cat_selected':0}
	return render(request, 'portfolio/index.html', context=context)
def about(request):
	return render(request, 'portfolio/about.html', {'menu':menu, 'title':'О сайте'})
def pageNotFound(request, exception):
	return HttpResponseNotFound("<h1>Страница не найдена</h1>")
def addpage(request):
	if request.method=='POST':
		form=AddPostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=AddPostForm()
	return render(request, 'portfolio/addpage.html', {'form':form,'menu':menu, 'title':'Добавление статьи'})
def contact(request):
	return HttpResponse("Обратная связь")
def login(request):
	return HttpResponse("Авторизация")
def show_post(request, post_slug):
	post=get_object_or_404(Portfolio, slug=post_slug)
	context={'post':post,
		'menu':menu,
		'place':post.place,
		'cat_selected':post.cat_id,}
	return render(request, 'portfolio/post.html', context=context)
def show_category(request, cat_id):
	posts=Portfolio.objects.filter(cat_id=cat_id)
	if len(posts)==0:
		raise Http404()
	context={'posts':posts,
		'menu':menu,
		'title':'Главная страница',
		'cat_selected':cat_id,}
	return render(request, 'portfolio/index.html', context=context)