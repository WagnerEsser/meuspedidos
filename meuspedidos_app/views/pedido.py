# coding:utf-8
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import View
from django.shortcuts import render
from meuspedidos_app.forms import PedidoCadForm
from meuspedidos_app.models import ProdutoModel, PedidoModel, ItemModel


class PedidoView(View):
    template = 'pedido.html'
    template_produtos = 'produtos.html'

    def get(self, request):
        context_dict = {}

        if request.session and 'pedido' in request.session:
            ItemModel.objects.filter(pedido=request.session['pedido']).delete()
            del request.session['pedido']
            PedidoModel.objects.filter(status=False).delete()

        form = PedidoCadForm()
        context_dict['form'] = form
        return render(request, self.template, context_dict)

    def post(self, request):
        context_dict = {}

        id = None
        form = PedidoCadForm(data=request.POST)
        if form.is_valid():
            obj = form.save()
            request.session['pedido'] = obj.id
            msg = 'Pedido iniciado!'
            tipo_msg = 'green'
            context_dict['produtos'] = ProdutoModel.objects.all()
        else:
            print(form.errors)
            msg = 'Algo deu errado!'
            tipo_msg = 'red'

        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return HttpResponseRedirect(reverse('produtos'))

    @classmethod
    def adicionar_item(self, id_produto, id_pedido):
        pedido = PedidoModel.objects.get(pk=id_pedido)
        produto = ProdutoModel.objects.get(pk=id_produto)

        item = ItemModel()
        item.pedido = pedido
        item.produto = produto
        item.preco = produto.preco_unitario
        item.quantidade = 1
        item.save()

        return HttpResponseRedirect(reverse('produtos'))
