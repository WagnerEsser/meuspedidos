from django.http import HttpResponse
from django.shortcuts import render

from meuspedidos_app.models import PedidoModel


def index(request, msg=None, tipo_msg=None):
    context_dict = {}
    context_dict['pedidos'] = PedidoModel.objects.all().order_by('-id')
    context_dict['msg'] = msg
    context_dict['tipo_msg'] = tipo_msg
    return render(request, "index.html", context_dict)
