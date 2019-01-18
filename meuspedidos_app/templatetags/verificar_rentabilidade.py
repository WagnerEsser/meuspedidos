from django import template
from django.template.defaultfilters import stringfilter

from meuspedidos_app.models import PedidoModel, ItemModel, ProdutoModel
from meuspedidos_app.views import ProdutoView

register = template.Library()


@register.filter
@stringfilter
def verificar_rentabilidade(id_produto):
    pedido = PedidoModel.objects.get(status=False)
    item = ItemModel.objects.filter(pedido=pedido, produto=id_produto)
    produto = ProdutoModel.objects.get(pk=id_produto)
    preco_unitario = produto.preco_unitario

    if item:
        item = item[0]
        preco_pago = ProdutoView.remover_zeros_final(item.preco)
        preco_unitario = ProdutoView.remover_ponto_decimal(preco_unitario)

        print(preco_unitario)
        print(preco_pago)

        if preco_pago > preco_unitario:
            return "Ótima"
        elif preco_pago >= preco_unitario * 0.9 and preco_pago <= preco_unitario:
            return "Boa"
        else:
            return "Ruim (Não será add no pedido)"
    return "não está no pedido"


register.filter('verificar_rentabilidade', verificar_rentabilidade)
