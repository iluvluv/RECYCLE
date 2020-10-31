from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('goods/goods_create/',views.goods_create,name="goods_create"),
    path('goods/kinds_list/',views.kinds_list,name="kinds_list"),
    path('goods/detail/',views.detail,name="detail"),
]