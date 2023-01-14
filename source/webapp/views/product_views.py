from webapp.forms import ProductForm
from webapp.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


class ProductList(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 3
    ordering = ['category', 'title']


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_view.html'


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk })


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk })


class ProductDelete(DeleteView):
    model = Product
    template_name = "product/product_delete.html"
    success_url = reverse_lazy('index')