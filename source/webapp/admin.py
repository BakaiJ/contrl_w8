from django.contrib import admin
from webapp.models import Product, Review
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'description']
    list_display_links = ['title']
    list_filter = ['category']
    search_fields = ['title']
    exclude = []
    readonly_fields = ['picture']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'review_text', 'rating', 'moderated', 'created_at', 'updated_at']
    exclude = []
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
