from django import template
from django.template.defaultfilters import stringfilter

from meuspedidos_app.models import PedidoModel, ItemModel

register = template.Library()


@register.filter
@stringfilter
def mostrar_valor_total(id_produto):
    pedido = PedidoModel.objects.get(status=False)
    item = ItemModel.objects.get(pedido=pedido, produto=id_produto)
    preco = str(item.preco*item.quantidade)[:-3]
    preco = preco[:-2] + ',' + preco[-2:]
    return preco


register.filter('mostrar_valor_total', mostrar_valor_total)


@register.filter
@stringfilter
def mostrar_valor_total_edit(item):
    pedido = PedidoModel.objects.get(status=False)
    item = ItemModel.objects.get(pedido=pedido, produto=id_produto)
    preco = str(item.preco*item.quantidade)[:-3]
    preco = preco[:-2] + ',' + preco[-2:]
    return preco


register.filter('mostrar_valor_total', mostrar_valor_total)
# @register.filter
# @stringfilter
# def mostrar_valor_total_edit(item):
#     pedido = PedidoModel.objects.get(status=False)
#     item = ItemModel.objects.get(pedido=pedido, produto=id_produto)
#     preco = str(item.preco*item.quantidade)[:-3]
#     preco = preco[:-2] + ',' + preco[-2:]
#     return preco
#
#
# register.filter('mostrar_valor_total', mostrar_valor_total)
