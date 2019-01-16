from django.contrib import admin

# Register your models here.
from meuspedidos_app.models import ClienteModel, PedidoModel, ProdutoModel, ItemModel

admin.site.register(ClienteModel)
admin.site.register(PedidoModel)
admin.site.register(ProdutoModel)
admin.site.register(ItemModel)