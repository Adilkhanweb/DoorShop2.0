from .models import *
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('comment', 'rate')


class AddToLikedForm(forms.ModelForm):
    class Meta:
        model = LikedProducts
        fields = '__all__'
