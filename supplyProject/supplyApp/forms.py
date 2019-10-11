from django.forms import ModelForm
from .models import PaintSupplyModel, BrushSupplyModel, CanvasSupplyModel


class PaintForm(ModelForm):
    class Meta:
        model = PaintSupplyModel
        exclude = ['user']


class BrushForm(ModelForm):
    class Meta:
        model = BrushSupplyModel
        exclude = ['user']


class CanvasForm(ModelForm):
    class Meta:
        model = CanvasSupplyModel
        exclude = ['user']
