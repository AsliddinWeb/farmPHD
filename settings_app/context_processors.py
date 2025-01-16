from .models import SeoSettings, Navbar, SocialNetwork

def seo_settings(request):
    try:
        seo = SeoSettings.objects.last()
    except SeoSettings.DoesNotExist:
        seo = None

    navbars = Navbar.objects.filter(parent__isnull=True).prefetch_related('submenu_items')
    social_networks = SocialNetwork.objects.all()


    return {
        'seo_settings': seo,
        'navbars': navbars,
        'social_networks': social_networks,
    }
