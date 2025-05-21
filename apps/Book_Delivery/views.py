from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _


class CustomAdminSite(AdminSite):
    site_header = _("Food Delivery Administration")
    site_title = _("Food Delivery Admin Portal")
    index_title = _("Welcome to Food Delivery Admin")


admin_site = CustomAdminSite(name='custom_admin')



class GlobalAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)


        if 'delete_selected' in actions:
            actions[ 'delete_selected' ] = (
                self.delete_selected,
                'delete_selected',
                _("Delete selected %(verbose_name_plural)s")
            )
        return actions


    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    mark_as_active.short_description = _("Mark selected as active")



admin.site = admin_site
admin.site.register = lambda model, admin_class=None: admin_site.register(model, admin_class or GlobalAdmin)