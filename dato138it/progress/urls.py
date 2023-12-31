from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page
urlpatterns = [
	path('', ProgressHome.as_view(), name='home'), 
	path('about/', about, name='about'),
	path('addpage/', AddPage.as_view(), name='add_page'),
	path('contact/', ContactFormView.as_view(), name='contact'),
	path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
	path('category/<slug:cat_slug>/', ProgressCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
	path('login/', LoginUser.as_view(), name='login'),
	path('logout/', logout_user, name='logout'),
]