from django.urls import path
from .import views



from django.urls import path
from . import views

urlpatterns = [
    path('', views.galleryphoto, name='gallery'),  # O'zgartirish
    path('add/', views.addphoto, name='add'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('detail/<int:pk>/', views.detailphoto, name='detail'),
    path('category/<int:category_id>/', views.galleryphoto, name='photo_list_by_category'),  # O'zgartirish
]



