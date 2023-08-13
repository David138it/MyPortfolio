from django.db import models
from django.urls import reverse
class Portfolio(models.Model):
	begin=models.DateTimeField(auto_now_add=False, verbose_name="Время создания")
	finish=models.DateTimeField(auto_now=False, verbose_name="Время изменения")
	place=models.CharField(max_length=255, verbose_name="Заголовок")
	slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	specialization=models.CharField(max_length=255, verbose_name="Специальность")
	responsibilities=models.TextField(blank=True, verbose_name="Обязанности")
	progress=models.TextField(blank=True, verbose_name="Текст статьи")
	scan=models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
	is_published=models.BooleanField(default=True, verbose_name="Публикация")
	cat=models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
	def __str__(self):
		return self.place
	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug':self.slug})
	class Meta:
		verbose_name='Опыт работы'
		verbose_name_plural='Опыт работы'
		ordering=['-begin','place']
class Category(models.Model):
	name=models.CharField(max_length=100, db_index=True, verbose_name="Категория")
	slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('category', kwargs={'cat_id':self.pk})
	class Meta:
		verbose_name='Категория'
		verbose_name_plural='Категории'
		ordering=['id']