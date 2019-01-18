from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def formatar_preco(preco):
    preco = preco[:-3]
    preco = preco[:-2] + ',' + preco[-2:]
    return preco


register.filter('formatar_preco', formatar_preco)
