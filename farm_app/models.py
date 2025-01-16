from django.contrib.auth.models import User
from django.db import models


class Farm(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Kimga tegishli", related_name='farm')
    name = models.CharField(max_length=100, verbose_name="Fermangiz nomi")
    location = models.CharField(max_length=255, verbose_name="Manzil")
    area_size = models.FloatField(verbose_name="Maydon o'lchami (gektar)")
    owner = models.CharField(max_length=255, verbose_name="Egasining ismi")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="So'nggi yangilanish")

    class Meta:
        verbose_name = "Fermangiz"
        verbose_name_plural = "Fermalar"

    def __str__(self):
        return self.name


class Product(models.Model):
    farm = models.ForeignKey(Farm, related_name='products', on_delete=models.CASCADE, verbose_name="Fermaga bog'lanish")
    image = models.ImageField(upload_to='images/products/', verbose_name="Rasm", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Mahsulot nomi")
    quantity = models.FloatField(verbose_name="Miqdori (tonna)")
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Birlik narxi")
    harvested_at = models.DateTimeField(verbose_name="Hosil olingan sana")

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return f"{self.name} - {self.farm.name}"


class Equipment(models.Model):
    farm = models.ForeignKey(Farm, related_name='equipments', on_delete=models.CASCADE,
                             verbose_name="Fermaga bog'lanish")
    name = models.CharField(max_length=100, verbose_name="Asbob nomi")
    model = models.CharField(max_length=100, verbose_name="Modeli")
    purchased_at = models.DateTimeField(verbose_name="Sotib olingan sana")
    last_maintenance = models.DateField(verbose_name="So'nggi texnik xizmat sanasi")

    class Meta:
        verbose_name = "Asbob"
        verbose_name_plural = "Asboblar"

    def __str__(self):
        return f"{self.name} - {self.farm.name}"


class Employee(models.Model):
    farm = models.ForeignKey(Farm, related_name='employees', on_delete=models.CASCADE,
                             verbose_name="Fermaga bog'lanish")
    first_name = models.CharField(max_length=100, verbose_name="Ismi")
    last_name = models.CharField(max_length=100, verbose_name="Familyasi")
    role = models.CharField(max_length=100, verbose_name="Lavozimi")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Oylik maosh")
    hired_at = models.DateTimeField(verbose_name="Ishga qabul qilingan sana")

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FarmExpense(models.Model):
    farm = models.ForeignKey(Farm, related_name='expenses', on_delete=models.CASCADE, verbose_name="Fermaga bog'lanish")
    expense_type = models.CharField(max_length=100, verbose_name="Xarajat turi")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miqdori")
    date = models.DateTimeField(verbose_name="Xarajat sanasi")

    class Meta:
        verbose_name = "Xarajat"
        verbose_name_plural = "Xarajatlar"

    def __str__(self):
        return f"{self.expense_type} - {self.farm.name}"


class FarmIncome(models.Model):
    farm = models.ForeignKey(Farm, related_name='incomes', on_delete=models.CASCADE, verbose_name="Fermaga bog'lanish")
    product = models.ForeignKey(Product, related_name='incomes', on_delete=models.CASCADE, verbose_name="Mahsulot")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Daromad miqdori")
    date = models.DateTimeField(verbose_name="Daromad sanasi")

    class Meta:
        verbose_name = "Daromad"
        verbose_name_plural = "Daromadlar"

    def __str__(self):
        return f"{self.product.name} - {self.farm.name}"
