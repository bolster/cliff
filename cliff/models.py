from django.db import models


class EmailTemplate(models.Model):
    name = models.TextField()
    subject = models.TextField(help_text="""
This field uses the Django template language:
<a href="https://docs.djangoproject.com/en/1.5/topics/templates/">
https://docs.djangoproject.com/en/1.5/topics/templates/</a>""")
    body_html = models.TextField(help_text="""
This field uses the Django template language:
<a href="https://docs.djangoproject.com/en/1.5/topics/templates/">
https://docs.djangoproject.com/en/1.5/topics/templates/</a>""")
    body_plain = models.TextField(help_text="""
This field uses the Django template language:
<a href="https://docs.djangoproject.com/en/1.5/topics/templates/">
https://docs.djangoproject.com/en/1.5/topics/templates/</a>""")

    def __unicode__(self):
        return self.name
