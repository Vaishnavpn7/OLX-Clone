from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, FormView, ListView, DetailView, View
from products.forms import RegistrationForm, LoginForm, ProductForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from products.models import Products, ProductImage, Category
from django.db.models import Count
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator


def signin_requrird(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'you must login')
            return redirect('signin')
        else:
            return fn(request, *args, **kwargs)

    return wrapper


decs = [signin_requrird, never_cache]


# @method_decorator(decs, name='dispatch')
# class IndexView(ListView):
#     template_name = 'index.html'
#     context_object_name = 'products'
#     model = Products


class SignUpView(CreateView):
    template_name = "register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request, "account created success fully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "account creation failed")
        return super().form_invalid(form)


class SigninView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def post(self, request, *args, **kw):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(request, username=uname, password=pwd)
            if user:
                login(request, user)
                return redirect('list')
            else:
                return render(request, self.template_name, {'form': form})


class ProductView(CreateView):
    template_name = 'post_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'product added')
        return super().form_valid(form)


# class ProductListView(ListView):
#     template_name = 'product_list.html'
#     context_object_name = 'products'
#     model = Products


# class ProductListView(View):

@signin_requrird
def productlist(request, category_slug=None):
    category = None
    productlist = Products.objects.all()
    catagorylist = Category.objects.annotate(total_products=Count('products'))

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        productlist = Products.objects.filter(category=category)

    template = 'product_list.html'
    context = {'products': productlist, 'catagory_list': catagorylist, 'category': category}
    return render(request, template, context)


# class ProductDetail(DetailView):
#     template_name = 'product_detail.html'
#     context_object_name = 'product'
#     pk_url_kwarg = 'id'
#     model = Products


# class ProductDetailView(View):

@signin_requrird
def productdetail(request, product_slug):
    productdetail = Products.objects.get(slug=product_slug)
    productimage = ProductImage.objects.filter(product=productdetail)
    template = 'product_detail.html'
    context = {'product_detail': productdetail, 'product_images': productimage}
    return render(request, template, context)


@method_decorator(decs, name='dispatch')
class MyProduct(ListView):
    model = Products
    template_name = 'my_product.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Products.objects.filter(owner=self.request.user)


def logout_view(request, *args, **kwargs):
    logout(request)
    messages.success(request, 'looged out')
    return redirect('signin')
