import requests

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from farm_app.forms import FarmForm, ProductForm
from farm_app.models import Farm, Product

from settings_app.models import Message

def home_page(request):
    return render(request, 'home.html')


@login_required(login_url='login_page')
def dashboard_page(request):
    # Check if the user has a farm associated with them
    try:
        farm = request.user.farm
    except Farm.DoesNotExist:
        farm = None

    if request.method == 'POST':
        # If farm exists, update it
        if farm:
            form = FarmForm(request.POST, instance=farm)
        else:
            form = FarmForm(request.POST)

        if form.is_valid():
            farm = form.save(commit=False)
            farm.user = request.user  # Associate the farm with the current user
            farm.save()
            messages.success(request, "Ferma ma'lumotlari muvaffaqiyatli saqlandi!")
            return redirect('dashboard_page')
        else:
            messages.error(request, "Ma'lumotlarni saqlashda xato yuz berdi.")
    else:
        form = FarmForm(instance=farm)

    return render(request, 'dashboard/home.html', {'form': form, 'farm': farm})

@login_required(login_url='login_page')
def products_page(request):

    try:
        farm = request.user.farm
    except Farm.DoesNotExist:
        farm = None

    products = Product.objects.all()

    ctx = {'farm': farm, 'products': products}

    return render(request, 'dashboard/products.html', ctx)


@login_required(login_url='login_page')
def add_product_page(request):
    if request.method == 'POST':
        try:
            farm = request.user.farm
        except Farm.DoesNotExist:
            farm = None

        print(farm)

        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.farm = farm
            product.save()
            return redirect('products_page')

    else:
        form = ProductForm()
    return render(request, 'dashboard/add_product.html', {'form': form})


def edit_product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_page')
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/add_product.html', {'form': form, 'product': product, 'edit': True})

def delete_product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products_page')
    return render(request, 'dashboard/delete_product.html', {'product': product})



def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard_page')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Xush kelibsiz!")
            return redirect('dashboard_page')  # Redirect to the dashboard after successful login
        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol noto'g'ri.")

    return render(request, 'auth/login.html')


def register_page(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('dashboard_page')  # Redirect to the dashboard if already logged in

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in immediately after registration
            messages.success(request, "Hisobingiz muvaffaqiyatli yaratildi!")
            return redirect('dashboard_page')  # Redirect to the dashboard after registration
        else:
            messages.error(request, "Hisob yaratishda xato yuz berdi. Iltimos, ma'lumotlaringizni tekshirib ko'ring.")
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message_text = request.POST.get('message')

        # Modelga saqlash
        new_message = Message.objects.create(name=name, phone=phone, message=message_text)
        new_message.save()

        # Telegram bot orqali yuborish
        telegram_token = 'YOUR_TELEGRAM_BOT_TOKEN'
        chat_id = 'YOUR_TELEGRAM_CHAT_ID'
        telegram_message = (
            f"Yangi xabar!\n\n"
            f"👤 Ism: {name}\n"
            f"📞 Telefon: {phone}\n"
            f"💬 Xabar: {message_text}"
        )

        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': telegram_message,
        }

        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
        except requests.exceptions.RequestException as e:
            messages.error(request, "Xabar yuborishda xatolik yuz berdi!")
            print(f"Telegram API xatoligi: {e}")

        return redirect('contact_page')

    return render(request, 'contact.html')