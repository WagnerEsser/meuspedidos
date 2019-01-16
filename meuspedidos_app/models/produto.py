# coding: utf-8
from django.db import models


class ProdutoModel(models.Model):
    nome = models.CharField(max_length=100)
    preco_unitario = models.DecimalField(max_digits=30, decimal_places=2)
    multiplo = models.IntegerField(default=1)

    def get_or_none(id):
        try:
            return ProdutoModel.objects.get(pk=id)
        except:
            return None

    def __unicode__(self):
        return '%s' % self.nome

    def __str__(self):
        return '%s' % self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = 'Produtos'
