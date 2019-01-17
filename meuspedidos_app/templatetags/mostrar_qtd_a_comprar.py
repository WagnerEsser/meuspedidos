from django import template
from django.template.defaultfilters import stringfilter

from meuspedidos_app.models import PedidoModel, ItemModel

register = template.Library()


@register.filter
@stringfilter
def mostrar_qtd_a_comprar(id_produto):
    pedido = PedidoModel.objects.get(status=False)
    return ItemModel.objects.get(pedido=pedido, produto=id_produto).quantidade


register.filter('mostrar_qtd_a_comprar', mostrar_qtd_a_comprar)
