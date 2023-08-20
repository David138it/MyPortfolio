from django import forms
from django.core.exceptions import ValidationError
from .models import *
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label="Категория не выбрана"
    class Meta:
        model=Portfolio
        fields=['place', 'slug', 'specialization', 'progress', 'scan', 'is_published', 'cat']
        widgets={
            'place':forms.TextInput(attrs={'class':'form-input'}),
            'progress':forms.Textarea(attrs={'cols':60,'rows':10}),
        }
    def clean_title(self):
        place=self.cleaned_data['place']
        if len(place)>200:
            raise ValidationError('Длина превышает 200 символов')
        return place