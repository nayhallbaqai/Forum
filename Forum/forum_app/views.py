from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
from forum_app.models import *


class IndexView(generic.ListView):
    template_name = 'forum_app/index.html'
    model = Category
    context_object_name = 'category_list'

class CategoryQuestionList(generic.DetailView):
    template_name = 'forum_app/catQuestionList.html'
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryQuestionList, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.filter(category=self.get_object())
        return context
