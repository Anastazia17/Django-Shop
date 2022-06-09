import django.forms as forms

from .models import Goods


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'supplier', 'price', 'measure_unit', 'date_receipt')
