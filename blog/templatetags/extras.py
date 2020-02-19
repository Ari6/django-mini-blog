from django import template
from django.core.files.storage import default_storage
from django.conf import settings

register = template.Library()

@register.filter(name='file_check')
def file_check(filepath):
    NOIMAGE = 'no-image.png'
    
    if default_storage.exists(filepath):
        return filepath
    else:
        return self.NOIMAGE