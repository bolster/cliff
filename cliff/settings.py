from django import get_version

DJANGO_VERSION = get_version()
MAJOR_MINOR_VERSION = '.'.join(DJANGO_VERSION.split('.')[0:2])
TEMPLATE_FIELD_HELP_TEXT = """
This field uses the Django template language:
<a href="https://docs.djangoproject.com/en/{version}/topics/templates/">
https://docs.djangoproject.com/en/{version}/topics/templates/</a>""".format(
    version=MAJOR_MINOR_VERSION)
