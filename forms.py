from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput
from .models import Comments, News
from django import forms
from .models import *


class NewCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'text']
        widgets = {
            "name": TextInput(attrs={'placeholder':'Enter your name'}),
            "email": TextInput(attrs={'placeholder':'Enter your email'}),
            "text": Textarea(attrs={'placeholder':'Enter your comment', }),
        }


class CreateAddForm(ModelForm):

    class Meta:
        model = Adds
        fields = ['name',  'text', 'email', 'phone']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter the name'}),
            'text': Textarea(attrs={'placeholder': 'Enter the text of your add', 'cols': 60, 'rows': 10}),
            'email': TextInput(attrs={'placeholder': 'Provide the email'}),
            'phone': TextInput(attrs={'placeholder': 'Provide the phone'}),
        }

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) > 200:
            raise ValidationError('The text is too long!')
        return text


class CreateNewArticle(ModelForm):
    class Meta:
        model = News
        fields = ['user', 'title', 'content', 'picture', 'category', 'tags']
        widgets = {
            'user': Select(attrs={'placeholder': 'Choose the category'}),
            'title': TextInput(attrs={'placeholder': 'Enter the title'}),
            'content': Textarea(attrs={'placeholder': 'Enter the content', 'cols': 60, 'rows': 10}),
            'picture': FileInput(attrs={'placeholder': 'Upload the picture'}),
            'category': Select(attrs={'placeholder': 'Choose the category'}),
            'tags': TextInput(attrs={'placeholder': 'Add tags'}),
        }

