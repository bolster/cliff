from django import forms
from django.contrib import admin

from .models import EmailTemplate
from .settings import TEMPLATE_FIELD_HELP_TEXT


class EmailTemplateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'size': '75'}),
        help_text=TEMPLATE_FIELD_HELP_TEXT)

    class Meta:
        model = EmailTemplate


class EmailTemplateAdmin(admin.ModelAdmin):
    form = EmailTemplateForm

admin.site.register(EmailTemplate, EmailTemplateAdmin)
