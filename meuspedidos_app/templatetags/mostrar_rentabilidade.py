from django import template
from django.template.defaultfilters import stringfilter

from meuspedidos_app.models import ItemModel, ProdutoModel, PedidoModel
from meuspedidos_app.views.funcoes import *

register = template.Library()


@register.filter
@stringfilter
def mostrar_rentabilidade(id_produto):
    pedido = PedidoModel.objects.get(status=False)
    produto = ProdutoModel.objects.get(pk=id_produto)
    item = ItemModel.objects.filter(pedido=pedido, produto=produto)

    if item:
        item = item[0]
        preco_unitario_produto = remover_ponto_decimal(produto.preco_unitario)
        preco_pago = remover_zeros_final(item.preco)

        rentabilidade = verificar_rentabilidade(preco_unitario_produto, preco_pago)

        if rentabilidade == 1:
            # Boa
            return "Boa"
        elif rentabilidade == 0:
            # Ruim
            return "Ruim"
        elif rentabilidade == 2:
            # Ótima
            return "Ótima"
    return "---"


register.filter('mostrar_rentabilidade', mostrar_rentabilidade)
