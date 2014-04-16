from django.db import models

from .settings import TEMPLATE_FIELD_HELP_TEXT


class EmailTemplate(models.Model):
    name = models.TextField()
    subject = models.TextField(help_text=TEMPLATE_FIELD_HELP_TEXT)
    body_html = models.TextField(help_text=TEMPLATE_FIELD_HELP_TEXT)
    body_plain = models.TextField(help_text=TEMPLATE_FIELD_HELP_TEXT)

    def __unicode__(self):
        return self.name
