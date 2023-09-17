from django.urls import path, re_path
from .views import *
urlpatterns = [
	#path('', index), #http://127.0.0.1:8000/women/
	#path('home/', index, name='home'), #http://127.0.0.1:8000/
	#path('', index, name='home'), #http://127.0.0.1:8000/
	path('', WomenHome.as_view(), name='home'), #http://127.0.0.1:8000/
	#path('cats/', categories), #http://127.0.0.1:8000/women/cats/
	#path('cats/', categories), #http://127.0.0.1:8000/cats/
	#path('cats/<int:catid>/', categories), #http://127.0.0.1:8000/cats/1/
	#re_path(r'^archive/(?P<year>[0-9]{4})/', archive), #http://127.0.0.1:8000/archive/2020/
	path('about/', about, name='about'), #http://127.0.0.1:8000/
	#path('addpage/', addpage, name='add_page'),
	path('addpage/', AddPage.as_view(), name='add_page'),
	path('contact/', contact, name='contact'),
	path('login/', login, name='login'),
	#path('post/<int:post_id>/', show_post, name='post'),
	#path('post/<slug:post_slug>/', show_post, name='post'),
	path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
	#path('category/<int:cat_id>/', show_category, name='category'),
	path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
	#path('register/', login, name='register'),
	path('register/', RegisterUser.as_view(), name='register'),
]