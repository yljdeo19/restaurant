from django.contrib import admin
from privacy_policy.models import PrivacyPolicy
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PrivacyPolicyAdmin(SummernoteModelAdmin):
    list_display = [field.name for field in PrivacyPolicy._meta.fields]

    class Meta:
        model = PrivacyPolicy


admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
