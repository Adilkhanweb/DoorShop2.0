from django.urls import path
from shop.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/details', DoorDetailView.as_view(), name='product_detail'),
    path('category/<slug:slug>', CategoryProductsView.as_view(), name='category'),
    path('add_review/<int:id>', AddReviewView, name='add_review'),
    path('change_review/<int:id>', ChangeReviewView, name='change_review'),
    path('delete_review/<int:id>', DeleteReviewView, name='delete_review'),
    path('liked/<int:id>', AddToLiked, name='like'),
    path('liked_products/<int:pk>', LikedProductsView.as_view(), name='liked_products'),
    path('test/', test, name='test'),
    path('contact/<int:id>', ContactView, name='contact_us'),
    path('questions/<int:id>', MyQuestions.as_view(), name='my_questions'),
]
