from django.db import models


class EmailTemplate(models.Model):
    name = models.TextField()
    subject = models.TextField()
    body_html = models.TextField()
    body_plain = models.TextField()

    def __unicode__(self):
        return self.name
