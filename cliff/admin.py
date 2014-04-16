from django import forms
from django.contrib import admin

from .models import EmailTemplate


class EmailTemplateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'size': '75'}), help_text="""
This field uses the Django template language:
<a href="https://docs.djangoproject.com/en/1.5/topics/templates/">
https://docs.djangoproject.com/en/1.5/topics/templates/</a>""")

    class Meta:
        model = EmailTemplate


class EmailTemplateAdmin(admin.ModelAdmin):
    form = EmailTemplateForm

admin.site.register(EmailTemplate, EmailTemplateAdmin)
