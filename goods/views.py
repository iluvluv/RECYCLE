from django.shortcuts import render, get_object_or_404
from account.models import *
from purchase.models import *
from .models import *
# Create your views here.

# 메인 전체리스트
def index(request):
    kinds_list = Goods.objects.all
    return render(request, "index.html", kinds_list)

# 종류별 리스트
def kinds_list(request, kinds):
    kinds_list = Goods.objects.filter(kinds=kinds)
    return render(request, "kinds_list.html", kinds_list)

#상세보기
def detail(request, goods_id):
    goods = get_object_or_404(Goods, pk=goods_id)
    return render(request, "detail.html", goods)

