from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, FormView, ListView
from products.forms import RegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from products.models import Products


class IndexView(TemplateView):
    template_name = 'index.html'


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
                return redirect('index')
            else:
                return render(request, self.template_name, {'form': form})


class ProductListView(ListView):
    template_name = 'product_list.html'
    context_object_name = 'products'
    model = Products
