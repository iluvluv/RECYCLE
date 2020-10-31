from django.shortcuts import render
from account.models import *
from purchase.models import *
from .models import *
# Create your views here.

# 메인 전체리스트
def index(request):
    return render(request, "index.html")

# 상품 만들기
def goods_create(request):
    return render(request, "goods_create.hrml")

# 종류별 리스트
def kinds_list(request):
    return render(request, "kinds_list.html")

#상세보기
def detail(request):
    return render(request, "detail.html")

