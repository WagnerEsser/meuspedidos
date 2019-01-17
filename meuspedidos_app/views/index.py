from django.http import HttpResponse
from django.shortcuts import render

from meuspedidos_app.models import PedidoModel


def index(request):
    context_dict = {}
    context_dict['pedidos'] = PedidoModel.objects.all()

    return render(request, "index.html", context_dict)
