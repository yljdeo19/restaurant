from .models import PrivacyPolicy


def policy_info(request):
    add = PrivacyPolicy.objects.filter(is_active=True).last()
    return locals()
