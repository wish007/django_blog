from django.contrib import admin
from blogapp.models import Article
from pagedown.widgets import AdminPagedownWidget
from django import forms

# Define your form here.
class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

# Register your models here.
admin.site.register(Article,ArticleAdmin)
