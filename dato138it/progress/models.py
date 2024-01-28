from django.db import models
from django.contrib.auth.models import User
class Progress(models.Model):
    spec=models.CharField(max_length=255, verbose_name="Должность")
    content=models.TextField(blank=True, verbose_name="Достижения")
    task=models.TextField(blank=True, verbose_name="Обязанности")
    place=models.TextField(blank=True, verbose_name="Место работы")
    begin=models.DateField(blank=True, verbose_name="Начало работы")
    finish=models.DateField(blank=True, verbose_name="Конец работы")
    doc=models.FileField(upload_to="file/%Y/%m/%d/", verbose_name="Файлы")
    time_create=models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update=models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published=models.BooleanField(default=True, verbose_name="Публикация")
    cat=models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    def __str__(self):
        return self.spec
class Category(models.Model):
    name=models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    def __str__(self):
        return self.name
