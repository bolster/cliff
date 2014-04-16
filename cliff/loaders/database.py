from django.template.base import TemplateDoesNotExist
from django.template.loader import BaseLoader

from ..models import EmailTemplate


class Loader(BaseLoader):
    is_usable = True
    template_fields = {
        'subject.txt': 'subject',
        'email.txt': 'body_plain',
        'email.html': 'body_html',
    }

    def load_template_source(self, template_name, template_dirs=None):
        template_path, template_field = template_name.rsplit('/', 1)

        if template_field not in self.template_fields:
            raise TemplateDoesNotExist(template_name)

        try:
            template = EmailTemplate.objects.get(name=template_path)
        except EmailTemplate.DoesNotExist:
            raise TemplateDoesNotExist(template_name)

        source = getattr(template, self.template_fields[template_field])

        return source
