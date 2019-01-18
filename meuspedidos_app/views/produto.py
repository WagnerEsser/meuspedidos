# coding:utf-8
from django.shortcuts import render
from django.views import View
from decimal import Decimal

from meuspedidos_app.models import ProdutoModel, ItemModel
from meuspedidos_app.views.funcoes import verificar_rentabilidade, remover_ponto_decimal, remover_zeros_final
from meuspedidos_app.views.pedido import PedidoView


class ProdutoView(View):

    @classmethod
    def Listar(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        existe_item_pedido = False
        itens = ItemModel.objects.filter(pedido=request.session['pedido'])

        if itens:
            for item in itens:
                preco_unitario_produto = remover_ponto_decimal(item.produto.preco_unitario)
                preco_pago = remover_zeros_final(item.preco)

                if verificar_rentabilidade(preco_unitario_produto, preco_pago) != 0:
                    existe_item_pedido = True
                    break

        context_dict['existe_item_pedido'] = existe_item_pedido
        context_dict['produtos'] = ProdutoModel.objects.all().order_by('nome')
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, 'produtos.html', context_dict)

    @classmethod
    def ListarProdutosAdmin(self, request):
        context_dict = {}

        context_dict['produtos'] = ProdutoModel.objects.all().order_by('nome')
        return render(request, 'produtos_admin.html', context_dict)

    @classmethod
    def AdicionarRemoverProduto(self, request, msg=None, tipo_msg=None):
        if request.session and 'pedido' in request.session:
            id_pedido = request.session['pedido']
            id_produto = request.POST.get('id_produto')
            produto = ProdutoModel.objects.get(pk=id_produto)
            qtd = request.POST.get('qtd')
            preco_pago = request.POST.get('preco_pago')

            if ItemModel.objects.filter(pedido=id_pedido, produto=id_produto):
                PedidoView.remover_item(id_pedido, id_produto)
                msg = "Item removido com sucesso."
                tipo_msg = "green"
            else:
                if not qtd or not preco_pago:
                    msg = "Os campos quantidade e preço devem ser preenchidos para adicionar um pedido"
                    tipo_msg = "red"
                elif int(qtd) <= 0 or Decimal(preco_pago.replace(',', '')) <= 0:
                    msg = "A quantidade e o preço devem ser maior que zero"
                    tipo_msg = "red"
                else:
                    qtd = int(qtd)

                    if qtd % produto.multiplo == 0:
                        if preco_pago.find(',') == -1:
                            preco_pago = preco_pago + ',00'
                        preco_pago = Decimal(preco_pago.replace(',', ''))
                        PedidoView.adicionar_item(id_pedido, id_produto, preco_pago, qtd)
                        msg = "Item adicionado com sucesso."
                        tipo_msg = "green"
                    else:
                        msg = "A quantidade tem que obedecer o número Múltiplo!"
                        tipo_msg = "red"
        else:
            msg = "Algo deu errado, tente novamente"
            tipo_msg = "red"

        return self.Listar(request, msg, tipo_msg)
