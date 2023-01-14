from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreate(LoginRequiredMixin, CreateView):
    template_name = 'review/create.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.article = product
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class = ReviewForm
    context_object_name = 'review'

    def has_permission(self):
        return self.request.user.has_perm('webapp.change_review') or self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_review') or self.get_object().user == self.request.user

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk })

