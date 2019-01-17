# coding: utf-8
from django.db import models
from meuspedidos_app.models import ClienteModel, ProdutoModel


class PedidoModel(models.Model):
    itens = models.ManyToManyField(ProdutoModel, through='ItemModel')
    cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, choices=((0, 'Aberto'), (1, 'Fechado')))

    def __unicode__(self):
        return '%s %s em %s' % (self.cliente.nome, self.cliente.sobrenome, self.data.strftime(u'%d/%m/%Y em %H:%M'))

    def __str__(self):
        return '%s %s em %s' % (self.cliente.nome, self.cliente.sobrenome, self.data.strftime(u'%d/%m/%Y em %H:%M'))

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
