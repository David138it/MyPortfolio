from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from captcha.fields import CaptchaField
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label="Категория не выбрана"
    class Meta:
        model=Progress
        fields=['title', 'slug', 'progr', 'photo', 'is_published', 'cat']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'progr':forms.Textarea(attrs={'cols':60,'rows':10}),
        }
    def clean_title(self):
        title=self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError('Длина превышает 200 символов')
        return title
class RegisterUserForm(UserCreationForm):
    username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    mail=forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-input'}))
    password1=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2=forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    class Meta:
        model=User
        fields=('username','mail','password1','password2')
class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    capatcha = CaptchaField()