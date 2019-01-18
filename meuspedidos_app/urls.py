from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

from meuspedidos_app.views import ProdutoView
from meuspedidos_app.views.pedido import PedidoView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^contato/$', TemplateView.as_view(template_name='contato.html'), name='contato'),

    url(r'^novo_pedido/$', PedidoView.as_view(), name='novo_pedido'),
    url(r'^produtos/$', ProdutoView.Listar, name='produtos'),
    url(r'^lista_produtos/$', ProdutoView.ListarProdutosAdmin, name='lista_produtos'),
    url(r'^add_remove_produto/$', ProdutoView.AdicionarRemoverProduto, name='add_remove_produto'),
    url(r'^finalizar_pedido/$', PedidoView.FinalizarPedido, name='finalizar_pedido'),
    url(r'^visualizar_pedido/(?P<id>\d+)/$', PedidoView.VisualizarPedido, name='visualizar_pedido'),

    # 404
    url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
