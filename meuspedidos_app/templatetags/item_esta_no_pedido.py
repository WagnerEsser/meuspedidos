from django import template
from django.template.defaultfilters import stringfilter

from meuspedidos_app.models import PedidoModel, ItemModel

register = template.Library()


@register.filter
@stringfilter
def item_esta_no_pedido(id_produto):
    pedido = PedidoModel.objects.get(status=False)
    if ItemModel.objects.filter(pedido=pedido, produto=id_produto):
        return True
    else:
        return False


register.filter('item_esta_no_pedido', item_esta_no_pedido)
