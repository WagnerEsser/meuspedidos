# coding: utf-8
from django import forms
from meuspedidos_app.models.cliente import ClienteModel
from meuspedidos_app.models.pedido import PedidoModel


class PedidoCadForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(required=True,
                                     empty_label="Selecione um cliente",
                                     queryset=ClienteModel.objects.all(),
                                     widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"}))

    class Meta:
        model = PedidoModel
        fields = '__all__'
        exclude = ('itens', 'data', 'status')
