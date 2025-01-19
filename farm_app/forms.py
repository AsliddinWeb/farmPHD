from django import forms
from .models import Farm, Product, Equipment, Employee, FarmExpense, FarmIncome


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'location', 'area_size', 'owner']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'area_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'quantity', 'price_per_unit', 'harvested_at']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_per_unit': forms.NumberInput(attrs={'class': 'form-control'}),
            'harvested_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }



class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['farm', 'name', 'model', 'purchased_at', 'last_maintenance']
        widgets = {
            'farm': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'purchased_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'last_maintenance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['farm', 'first_name', 'last_name', 'role', 'salary', 'hired_at']
        widgets = {
            'farm': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'hired_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


class FarmExpenseForm(forms.ModelForm):
    class Meta:
        model = FarmExpense
        fields = ['farm', 'expense_type', 'amount', 'date']
        widgets = {
            'farm': forms.Select(attrs={'class': 'form-control'}),
            'expense_type': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


class FarmIncomeForm(forms.ModelForm):
    class Meta:
        model = FarmIncome
        fields = ['farm', 'product', 'amount', 'date']
        widgets = {
            'farm': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
