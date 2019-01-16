# coding: utf-8
from django.db import models
from meuspedidos_app.models import ProdutoModel, PedidoModel


class ItemModel(models.Model):
    produto = models.ForeignKey(ProdutoModel, on_delete=models.CASCADE)
    pedido = models.ForeignKey(PedidoModel, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    # trocar para preco_pago
    quantidade = models.IntegerField(default=1)

    def rentabilidade(self):
        if self.preco > self.produto.preco_unitario:
            return 2
        elif self.preco < float(self.produto.preco_unitario) * 0.9:
            return 0
        else:
            return 1

    def get_or_none(id):
        try:
            return ItemModel.objects.get(pk=id)
        except:
            return None

    def __str__(self):
        return '(%s) %s' % (self.quantidade, self.produto.nome)

    class Meta:
        verbose_name_plural = 'Itens'
