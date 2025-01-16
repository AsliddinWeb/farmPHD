from django.db import models
from django.template.defaultfilters import default


class SeoSettings(models.Model):
    site_name = models.CharField(max_length=255, help_text="Sayt nomi", verbose_name="Sayt nomi")
    site_description = models.TextField(help_text="Saytning qisqacha tavsifi", verbose_name="Sayt tavsifi")
    site_keywords = models.CharField(max_length=255, help_text="Sayt uchun kalit so'zlar, vergul bilan ajratilgan",
                                     verbose_name="Kalit so'zlar")
    site_author = models.CharField(max_length=255, blank=True, null=True, help_text="Sayt muallifi",
                                   verbose_name="Sayt muallifi")

    site_logo = models.ImageField(upload_to='seo_settings/logos/', blank=True, null=True, help_text="Sayt logotipi",
                                  verbose_name="Sayt logotipi")
    site_css = models.TextField(blank=True, null=True, help_text="Sayt CSS sozlamalari",
                                  verbose_name="Sayt CSS sozlamalari")

    site_favicon = models.ImageField(upload_to='seo_settings/favicon/', blank=True, null=True,
                                     help_text="Saytning favicon rasm fayli", verbose_name="Sayt faviconi")

    created_at = models.DateTimeField(auto_now_add=True, help_text="Sozlama yaratish vaqti",
                                      verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, help_text="Sozlamalar oxirgi marta yangilangan vaqt",
                                      verbose_name="Yangilangan vaqt")

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "SEO Sozlama"
        verbose_name_plural = "SEO Sozlamalari"


class Navbar(models.Model):
    title = models.CharField(max_length=100, verbose_name="Navbar nomi")
    link = models.CharField(max_length=255, verbose_name="Havola")

    is_submenu = models.BooleanField(default=False, verbose_name="Ichma ich menyumi?")

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='submenu_items',
        blank=True,
        null=True,
        verbose_name="Parentni belgilash"
    )

    created_at = models.DateTimeField(auto_now_add=True, help_text="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, help_text="Yangilangan vaqti")

    class Meta:
        verbose_name = "Navbar"
        verbose_name_plural = "Navbarlar"

    def __str__(self):
        return self.title


class SocialNetwork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Ijtimoiy tarmoq nomi")
    link = models.CharField(max_length=200, verbose_name="Havola")
    i_class = models.CharField(max_length=100, verbose_name="Ikonka klassi")

    class Meta:
        verbose_name = "Ijtimoiy tarmoq"
        verbose_name_plural = "Ijtimoiy tarmoqlar"

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism familiya")
    phone = models.CharField(max_length=255, verbose_name="Telefon raqam")
    message = models.TextField(verbose_name="Xabar")
    is_checked = models.BooleanField(default=False, verbose_name="O'qilganmi?")

    def __str__(self):
        return f"{self.name} - {self.message}"

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
