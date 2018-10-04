from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class AdminSite(admin.AdminSite):
    index_template = 'djvuesax/admin/home.html'