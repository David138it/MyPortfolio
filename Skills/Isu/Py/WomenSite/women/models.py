from django.db import models
from django.urls import reverse
# Create your models here.
class Women(models.Model):
	"""docstring for Women"""
	title=models.CharField(max_length=255, verbose_name="Заголовок")
	slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	content=models.TextField(blank=True, verbose_name="Текст статьи")
	photo=models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
	time_create=models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
	time_update=models.DateTimeField(auto_now=True, verbose_name="Время изменения")
	is_published=models.BooleanField(default=True, verbose_name="Публикация")
	#cat=models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")
	cat=models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
	#owner = models.ForeignKey('auth.User', related_name='womens', on_delete=models.CASCADE)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug':self.slug})
	class Meta:
		verbose_name='Известные женщины'
		verbose_name_plural='Известные женщины'
		#ordering=['time_create','title']
		#ordering=['-time_create','title']
		ordering=['id']
class Category(models.Model):
	name=models.CharField(max_length=100, db_index=True, verbose_name="Категория")
	slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		#return reverse('category', kwargs={'cat_id':self.pk})
		return reverse('category', kwargs={'cat_slug':self.slug})
	class Meta:
		verbose_name='Категория'
		verbose_name_plural='Категории'
		ordering=['id']