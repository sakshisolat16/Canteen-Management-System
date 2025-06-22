from django.contrib import admin
from .models import Product, Contact, Orders, OrderUpdate

# Import the UserAdmin class if you want to override it (optional)
from django.contrib.auth.admin import UserAdmin

# Admin Customizations for Models
class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'update_desc', 'timestamp')
    list_filter = ['timestamp']

    def has_delete_permission(self, request, obj=None):
        return False


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'userId', 'name', 'email', 'timestamp')
    list_filter = ['timestamp']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price')
    list_filter = ['category']
    search_fields = ['product_name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'email', 'timestamp')
    list_filter = ['timestamp']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

# Register models with the customized admin interface
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderUpdate, OrderUpdateAdmin)

# Admin Site Customizations
admin.site.site_header = "The SandipEatsNow Admin"
admin.site.index_title = "The SandipEatsNow Administration"
admin.site.site_title = "The SandipEatsNow Admin"

# Add custom CSS to the admin interface
class CustomAdminSite(admin.AdminSite):
    class Media:
        css = {
            'all': ('shop/assets/css/adminstyle.css',)  # Link to custom CSS file
        }

# Use CustomAdminSite instead of the default admin
admin_site = CustomAdminSite(name='custom_admin')
