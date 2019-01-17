# coding:utf-8
from django.shortcuts import render
from django.views import View
from meuspedidos_app.models import ProdutoModel, ItemModel
from meuspedidos_app.views.pedido import PedidoView


class ProdutoView(View):

    @classmethod
    def Listar(self, request):
        context_dict = {}
        context_dict['produtos'] = ProdutoModel.objects.all().order_by('nome')
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
            preco_pago = request.POST.get('preco_pago')
            qtd = request.POST.get('qtd')

            if ItemModel.objects.filter(pedido=id_pedido, produto=id_produto):
                PedidoView.remover_item(id_pedido, id_produto)
            else:
                PedidoView.adicionar_item(id_pedido, id_produto, preco_pago, qtd)

        return self.Listar(request)
