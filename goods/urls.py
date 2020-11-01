from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('goods/kinds_list/<str:kinds_name>',views.kinds_list,name="kinds_list"),
    path('goods/detail/<int:id>',views.detail,name="detail"),
    path('update/', views.update, name="update"),
    path('show/', views.show, name="show"),
]