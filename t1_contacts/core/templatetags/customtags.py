from django.core.urlresolvers import reverse
from django import template

register = template.Library()

@register.simple_tag
def edit_link(obj=''):
    if not obj:
        raise template.TemplateSyntaxError, "'edit_link' tag requires object as argument"

    url = reverse('admin:%s_%s_change' %(obj._meta.app_label,  obj._meta.module_name),  args=[obj.id] )
    return u'<a href="%s">Edit %s</a>' %(url,  obj.__unicode__())
