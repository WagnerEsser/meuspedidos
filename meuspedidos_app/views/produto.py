# coding:utf-8
from django.shortcuts import render
from django.views import View
from meuspedidos_app.models import ProdutoModel, ItemModel
from meuspedidos_app.views.pedido import PedidoView


class ProdutoView(View):

    @classmethod
    def Listar(self, request, msg=None, tipo_msg=None):
        context_dict = {}

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
    def AdicionarRemoverProduto(self, request):
        if request.session and 'pedido' in request.session:
            id_pedido = request.session['pedido']
            id_produto = request.POST.get('id_produto')
            produto = ProdutoModel.objects.get(pk=id_produto)
            qtd = request.POST.get('qtd')

            if ItemModel.objects.filter(pedido=id_pedido, produto=id_produto):
                PedidoView.remover_item(id_pedido, id_produto)
            else:
                preco_pago = request.POST.get('preco_pago')
                from decimal import Decimal
                preco_pago = Decimal(preco_pago.replace(',', ''))

                qtd = int(qtd)

                if qtd % produto.multiplo == 0:
                    PedidoView.adicionar_item(id_pedido, id_produto, preco_pago, qtd)
                else:
                    return self.Listar(request, msg="A quantidade tem que obedecer o número Múltiplo!", tipo_msg="red")

        return self.Listar(request)
