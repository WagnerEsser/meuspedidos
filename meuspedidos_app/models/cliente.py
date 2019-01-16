# coding: utf-8
from django.db import models


class ClienteModel(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s %s' % (self.nome, self.sobrenome)

    def __str__(self):
        return '%s %s' % (self.nome, self.sobrenome)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
