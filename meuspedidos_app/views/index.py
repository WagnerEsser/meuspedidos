from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {}

    return render(request, "index.html", context_dict)
