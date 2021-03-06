from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.views import generic

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image_source']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
    attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }