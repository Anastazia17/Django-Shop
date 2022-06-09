from django.urls import path

from .views import GoodsModelFormView, GoodsModelListView

urlpatterns = [
    path('', GoodsModelListView.as_view(), name='goods'),
    path('create/', GoodsModelFormView.as_view(), name='good_create')
]
