from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView

from .forms import GoodsForm
from .models import Goods


class GoodsModelListView(ListView, FormView):
    form_class = GoodsForm
    template_name = 'goods_list.html'
    # Группировка запросов для OneToOne
    queryset = Goods.objects.select_related('supplier').all()
    # Группировка запросов для ManyToMany
    # queryset = Goods.objects.prefetch_related('supplier').all()


class GoodsModelFormView(FormView, CreateView):
    template_name = 'good_create.html'
    form_class = GoodsForm

    success_url = reverse_lazy('goods')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            data = {
                'form_is_valid': False,
                'html_form': response.rendered_content
            }
            return JsonResponse(data)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'form_is_valid': True,
                'html_good_list': render_to_string(
                    'inc/partial_goods_list.html', {
                        'object_list': Goods.objects.select_related(
                            'supplier').all()
                    }),
            }
            return JsonResponse(data)
        else:
            return response
