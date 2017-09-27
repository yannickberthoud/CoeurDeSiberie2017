from django import template
from django.core.urlresolvers import reverse
from snake.models import Family

register = template.Library()

@register.inclusion_tag('snake/templatetags/filter.html', takes_context=True)
def family(context):
        request = context['request']
        families = Family.objects.order_by('name').distinct()
        return {'request': request, 'families': families}