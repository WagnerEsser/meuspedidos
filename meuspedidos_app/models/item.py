# coding: utf-8
from django.db import models
from meuspedidos_app.models import ProdutoModel, PedidoModel


class ItemModel(models.Model):
    produto = models.ForeignKey(ProdutoModel, on_delete=models.CASCADE)
    pedido = models.ForeignKey(PedidoModel, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return '(%s) %s' % (self.quantidade, self.produto.nome)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
