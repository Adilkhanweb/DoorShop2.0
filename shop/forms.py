from .models import *
from django import forms


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('comment', 'rate')
