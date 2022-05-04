from django.urls import path
from shop.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/details', DoorDetailView.as_view(), name='product_detail'),
    path('category/<slug:slug>', CategoryProductsView.as_view(), name='category'),
    path('add_review/<int:id>', AddReviewView, name='add_review'),
    path('test/', test, name='test'),
]
