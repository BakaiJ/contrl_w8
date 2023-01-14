from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
CATEGORY_CHOICES = [('Clothes', 'Одежда'), ('Tools', 'Инструменты'), ('Equipments', 'Экиперовка')]


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                              verbose_name="Категория")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Картинка')

    def __str__(self):
        return f'{self.pk}. {self.title}. {self.category}. {self.picture}'

    def get_absolute_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.pk})

    def get_average(self):
        product = Product.objects.get(pk=self.pk)
        average = 0
        avg_list = []
        for review in product.product_reviews.all():
            if review.moderated:
                average += review.grade
                avg_list.append(review.grade)
        if average:
            return average / len(avg_list)
        return average

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Review(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='reviews', blank=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='reviews', default=1,
                                verbose_name='Продукт')
    review_text = models.TextField(max_length=3000, blank=False, null=False, verbose_name='Отзыв')
    rating = models.IntegerField(null=False, blank=False, default=0, verbose_name='Оценка')
    moderated = models.BooleanField(null=False, blank=True, verbose_name="Модерирован")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        permissions = [
            ('can_add_moderated_to_the_review', 'Может модерировать отзыв'),
            ('can_view_moderated_to_the_review', 'Может видеть немодерированные отзывы'),
        ]
    # def __str__(self):
    #     return f'{self.pk}'
