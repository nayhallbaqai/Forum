from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

class IndexView(View):

    greeting = "Hello World!"

    def get(self, request):
        return HttpResponse(self.greeting)
