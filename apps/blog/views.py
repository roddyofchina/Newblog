from django.shortcuts import render
from django.views.generic.base import View
from .models import NavigationMenu,Article
# Create your views here.


class IndexView(View):
    def get(self,request):
        menu_list = NavigationMenu.objects.all()
        article_list = Article.objects.all()
        return  render(request,'index.html',locals())
