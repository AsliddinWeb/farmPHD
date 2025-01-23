from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Sarlavha"))

    class Meta:
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")

    def get_absolute_url(self):
        return reverse('category_detail_page', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class News(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='news', verbose_name=_("Kategoriya"))

    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    body = models.TextField(verbose_name=_("Matn"))

    image = models.ImageField(upload_to='news_images/', verbose_name=_("Asosiy rasm"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    class Meta:
        verbose_name = _("Yangilik")
        verbose_name_plural = _("Yangiliklar")
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail_page', kwargs={'pk': self.pk})
