from django.contrib import admin
from .models import Farm, Product, Equipment, Employee, FarmExpense, FarmIncome


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'area_size', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'owner')
    list_filter = ('created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm', 'quantity', 'price_per_unit', 'harvested_at')
    search_fields = ('name',)
    list_filter = ('farm',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm', 'model', 'purchased_at', 'last_maintenance')
    search_fields = ('name', 'model')
    list_filter = ('farm',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'salary', 'hired_at')
    search_fields = ('first_name', 'last_name', 'role')
    list_filter = ('role',)


@admin.register(FarmExpense)
class FarmExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_type', 'farm', 'amount', 'date')
    search_fields = ('expense_type',)
    list_filter = ('farm',)


@admin.register(FarmIncome)
class FarmIncomeAdmin(admin.ModelAdmin):
    list_display = ('product', 'farm', 'amount', 'date')
    search_fields = ('product__name',)
    list_filter = ('farm',)
