from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def status_pedido(status):
    if status == "False":
        return "Aberto"
    else:
        return "Fechado"


register.filter('status_pedido', status_pedido)
