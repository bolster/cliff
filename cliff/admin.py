from django import forms
from django.contrib import admin
from django_ace import AceWidget

from .models import EmailTemplate
from .settings import TEMPLATE_FIELD_HELP_TEXT


class CliffAceWidget(AceWidget):

    class Media:
        css = {
            'all': ['cliff/emailtemplateform.css'],
        }


class EmailTemplateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'size': '75'}),
        help_text=TEMPLATE_FIELD_HELP_TEXT)
    body_html = forms.CharField(
        widget=CliffAceWidget(mode='django'),
        help_text=TEMPLATE_FIELD_HELP_TEXT)
    body_plain = forms.CharField(
        widget=CliffAceWidget(mode='django'),
        help_text=TEMPLATE_FIELD_HELP_TEXT)

    class Meta:
        model = EmailTemplate


class EmailTemplateAdmin(admin.ModelAdmin):
    form = EmailTemplateForm

admin.site.register(EmailTemplate, EmailTemplateAdmin)
