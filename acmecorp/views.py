# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django Pssilva"
        params["title"] = "AdminLTE | Fatiando"
        return render(request, 'admin-lte.html', params)

    def post(self, request):
        return HttpResponse('I am called from a post Request')
