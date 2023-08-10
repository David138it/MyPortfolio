from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.
#def index(request): #HttpRequest
#	return HttpResponse("Страница приложения Women")
#menu=["О сайте", "Добавить статью", "Обратная связь", "Войти"]
menu=[{'title':"О сайте", 'url_name':'about'}, 
	{'title':"Добавить статью", 'url_name':'add_page'},
	{'title':"Обратная связь", 'url_name':'contact'},
	{'title':"Войти", 'url_name':'login'}]
def index(request):
	#return render(request, 'women/index.html', {'title':'Главная страница'})
	posts=Women.objects.all()
	#cats=Category.objects.all()
	context={'posts':posts, 
		#'cats':cats,
		'menu':menu, 
		'title':'Главная страница',
		'cat_selected':0}
	return render(request, 'women/index.html', context=context)
def about(request):
	return render(request, 'women/about.html', {'menu':menu, 'title':'О сайте'})
#def categories(request):
	#return HttpResponse("<h1>Статьи по категориям</h1>")
#def categories(request, catid):
	#print(request.GET) #http://127.0.0.1:8000/cats/1/?name=Gagarina&type=pop
	#if(request.GET):
		#print(request.GET) #http://127.0.0.1:8000/cats/1
	#if(request.POST):
		#print(request.POST) 
	#return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")
#def archive(request, year):
	#if int(year)>2020:
		#raise Http404() #http://127.0.0.1:8000/archive/2022/
		#return redirect('/', )
		#return redirect('home', permanent=True)
	#return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>") #http://127.0.0.1:8000/archive/2020/
def pageNotFound(request, exception):
	return HttpResponseNotFound("<h1>Страница не найдена</h1>")
def addpage(request):
	return HttpResponse("Добавление статьи")
def contact(request):
	return HttpResponse("Обратная связь")
def login(request):
	return HttpResponse("Авторизация")
#def show_post(request, post_id):
def show_post(request, post_slug):
	#return HttpResponse(f"Отображение статьи с id = {post_id}")
	#post=get_object_or_404(Women, pk=post_id)
	post=get_object_or_404(Women, slug=post_slug)
	context={'post':post,
		'menu':menu,
		'title':post.title,
		'cat_selected':post.cat_id,}
	return render(request, 'women/post.html', context=context)
#def show_category(request, cat_id):
	#return HttpResponse(f"Отображение категории с id = {cat_id}")
def show_category(request, cat_id):
	posts=Women.objects.filter(cat_id=cat_id)
	#cats=Category.objects.all()
	if len(posts)==0:
		raise Http404()
	context={'posts':posts,
		#'cats':cats,
		'menu':menu,
		'title':'Главная страница',
		'cat_selected':cat_id,}
	return render(request, 'women/index.html', context=context)