from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register', views.SignUpView.as_view(), name='register'),
    path('login', views.SigninView.as_view(), name='signin'),
    path('home', views.IndexView.as_view(), name='index'),
    path('list', views.ProductListView.as_view())
]
