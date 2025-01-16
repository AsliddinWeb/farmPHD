# Generated by Django 5.1.4 on 2025-01-10 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeoSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(help_text='Sayt nomi', max_length=255, verbose_name='Sayt nomi')),
                ('site_description', models.TextField(help_text='Saytning qisqacha tavsifi', verbose_name='Sayt tavsifi')),
                ('site_keywords', models.CharField(help_text="Sayt uchun kalit so'zlar, vergul bilan ajratilgan", max_length=255, verbose_name="Kalit so'zlar")),
                ('site_author', models.CharField(blank=True, help_text='Sayt muallifi', max_length=255, null=True, verbose_name='Sayt muallifi')),
                ('site_logo', models.ImageField(blank=True, help_text='Sayt logotipi', null=True, upload_to='seo_settings/logos/', verbose_name='Sayt logotipi')),
                ('site_css', models.TextField(blank=True, help_text='Sayt CSS sozlamalari', null=True, verbose_name='Sayt CSS sozlamalari')),
                ('site_favicon', models.ImageField(blank=True, help_text='Saytning favicon rasm fayli', null=True, upload_to='seo_settings/favicon/', verbose_name='Sayt faviconi')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Sozlama yaratish vaqti', verbose_name='Yaratilgan vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Sozlamalar oxirgi marta yangilangan vaqt', verbose_name='Yangilangan vaqt')),
            ],
            options={
                'verbose_name': 'SEO Sozlama',
                'verbose_name_plural': 'SEO Sozlamalari',
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Ijtimoiy tarmoq nomi')),
                ('link', models.CharField(max_length=200, verbose_name='Havola')),
                ('i_class', models.CharField(max_length=100, verbose_name='Ikonka klassi')),
            ],
            options={
                'verbose_name': 'Ijtimoiy tarmoq',
                'verbose_name_plural': 'Ijtimoiy tarmoqlar',
            },
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Navbar nomi')),
                ('link', models.CharField(max_length=255, verbose_name='Havola')),
                ('is_submenu', models.BooleanField(default=False, verbose_name='Ichma ich menyumi?')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Yangilangan vaqti')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submenu_items', to='settings_app.navbar', verbose_name='Parentni belgilash')),
            ],
            options={
                'verbose_name': 'Navbar',
                'verbose_name_plural': 'Navbarlar',
            },
        ),
    ]
