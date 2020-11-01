from django.shortcuts import render, get_object_or_404
from account.models import *
from purchase.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

class Data:
    value = ""

# 메인 전체리스트
def index(request):
    object_all = Goods.objects.all
    return render(request, "index.html", {"object_all":object_all})


# 종류별 리스트
@login_required
def kinds_list(request, kinds_name):
    kinds_list = Goods.objects.filter(kinds=kinds_name)
    return render(request, "kinds_list.html", {"kinds_list":kinds_list, "kinds_name":kinds_name})

#상세보기
@login_required
def detail(request, id):
    goods = get_object_or_404(Goods, pk=id)
    return render(request, "detail.html", {"goods":goods})

@csrf_exempt
def show(request):
    dt = {"value": Data.value}
    return HttpResponse(content=json.dumps(dt))


@csrf_exempt
def update(request):
    data = request.POST['data']
    if len(data) != 0:
        Data.value = request.POST['data']
        print(Data.value)
    return HttpResponse()