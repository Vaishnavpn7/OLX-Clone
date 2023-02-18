from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('register', views.SignUpView.as_view(), name='register'),
    path('', views.SigninView.as_view(), name='signin'),
    path('logout', views.logout_view, name='signout'),
    # path('home', views.IndexView.as_view(), name='index'),
    path('add',views.ProductView.as_view(), name='add_product'),
    path('list', views.productlist, name='list'),
    path('list/<slug:category_slug>', views.productlist, name='list_category'),

    # path('list', views.ProductListView.as_view(), name='list'),
    # path('detail/<int:id>', views.ProductDetail.as_view(), name='detail')
    path('detail/<int:id>', views.productdetail, name='detail'),
    path('myproduct', views.MyProduct.as_view(), name='myproduct')
]
