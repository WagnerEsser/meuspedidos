# coding:utf-8
from django.shortcuts import render
from django.views import View
from meuspedidos_app.models import ProdutoModel
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
    def AdicionarProduto(self, request, id):
        if request.session and 'pedido' in request.session:
            PedidoView.adicionar_item(id, request.session['pedido'])
        return self.Listar(request)
