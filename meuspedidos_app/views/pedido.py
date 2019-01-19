# coding:utf-8
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import View
from django.shortcuts import render
from meuspedidos_app.forms import PedidoCadForm
from meuspedidos_app.models import ProdutoModel, PedidoModel, ItemModel
from meuspedidos_app.views.index import index
from meuspedidos_app.views.funcoes import *


class PedidoView(View):
    template = 'pedido.html'
    template_produtos = 'produtos.html'
    template_view = 'pedido_view.html'

    def get(self, request):
        context_dict = {}

        if request.session and 'pedido' in request.session:
            ItemModel.objects.filter(pedido=request.session['pedido']).delete()
            del request.session['pedido']
            PedidoModel.objects.filter(status=False).delete()

        if request.session and 'pedido_edit' in request.session:
            pedido = PedidoModel.objects.get(pk=request.session['pedido_edit'])
            pedido.status = True
            pedido.save()
            del request.session['pedido_edit']

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
    def adicionar_item(self, id_pedido, id_produto, preco_pago, qtd):
        pedido = PedidoModel.objects.get(pk=id_pedido)
        produto = ProdutoModel.objects.get(pk=id_produto)

        item = ItemModel()
        item.pedido = pedido
        item.produto = produto
        item.preco = preco_pago
        item.quantidade = qtd
        item.save()

        return HttpResponseRedirect(reverse('produtos'))

    @classmethod
    def remover_item(self, id_pedido, id_produto):
        ItemModel.objects.filter(pedido=id_pedido, produto=id_produto).delete()

        return HttpResponseRedirect(reverse('produtos'))

    @classmethod
    def FinalizarPedido(self, request):
        if request.session:
            if 'pedido' in request.session:
                id_pedido = request.session['pedido']
            elif 'pedido_edit' in request.session:
                id_pedido = request.session['pedido_edit']
            else:
                id_pedido = None

            if id_pedido:
                pedido = PedidoModel.objects.get(pk=id_pedido)

                self.remover_itens_nao_rentaveis(id_pedido)

                pedido.status = True
                pedido.save()

                if 'pedido' in request.session:
                    del request.session['pedido']
                elif 'pedido_edit' in request.session:
                    del request.session['pedido_edit']

                msg = "Pedido realizado com sucesso"
                tipo_msg = "green"
            else:
                msg = "Algo deu errado, tente novamente!"
                tipo_msg = "red"
        else:
            msg = "Algo deu errado, tente novamente!"
            tipo_msg = "red"

        return index(request, msg, tipo_msg)

    @classmethod
    def remover_itens_nao_rentaveis(self, id_pedido):
        itens = ItemModel.objects.filter(pedido=id_pedido)

        for item in itens:
            produto = ProdutoModel.objects.get(pk=item.produto.pk)
            preco_unitario_produto = remover_ponto_decimal(produto.preco_unitario)
            preco_pago = remover_zeros_final(item.preco)

            if verificar_rentabilidade(preco_unitario_produto, preco_pago) == 0:
                item.delete()

        return

    @classmethod
    def VisualizarPedido(self, request, id):
        context_dict = {}

        pedido = PedidoModel.objects.get(pk=id)
        itens = ItemModel.objects.filter(pedido=id)

        for i, item in enumerate(itens):
            preco = str(item.preco * item.quantidade)[:-3]
            preco = preco[:-2] + ',' + preco[-2:]
            itens[i].valor_total = preco

        context_dict['pedido'] = pedido
        context_dict['itens'] = itens
        return render(request, self.template_view, context_dict)
