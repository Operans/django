from django import forms
from .models import OrderCL

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderCL
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

