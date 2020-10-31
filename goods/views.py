from django.shortcuts import render, get_object_or_404
from account.models import *
from purchase.models import *
from .models import *
# Create your views here.

# 메인 전체리스트
def index(request):
    object_all = Goods.objects.all
    return render(request, "index.html", {"object_all":object_all})


# 종류별 리스트
def kinds_list(request, kinds_name):
    kinds_list = Goods.objects.filter(kinds=kinds_name)
    return render(request, "kinds_list.html", {"kinds_list":kinds_list, "kinds_name":kinds_name})

#상세보기
def detail(request, goods_id):
    goods = get_object_or_404(Goods, pk=goods_id)
    return render(request, "detail.html", {"goods":goods})

