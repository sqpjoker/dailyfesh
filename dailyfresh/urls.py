# -*-coding:utf-8-*-
from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url('admin/', admin.site.urls),
    url('tinymce/', include('tinymce.urls')),  # 富文本编辑器
    url('search/', include('haystack.urls')),  # 全文检索框架
    url('user/', include('user.urls', namespace='user')),  # 用户模块
    url('cart/', include('cart.urls', namespace='cart')),  # 购物车模块
    url('order/', include('order.urls', namespace='order')),  # 订单模块
    url('', include('goods.urls', namespace='goods')),  # 商品模块
]
