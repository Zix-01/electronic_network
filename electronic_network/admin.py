from django.contrib import admin
from .models import Factory, RetailNetwork, Entrepreneur, Contacts, Product


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'supplier', 'outstanding_debt', 'creation_time']
    list_filter = ('contact_info__city',)
    actions = ['clear_outstanding_debt']

    def clear_outstanding_debt(self, request, queryset):
        for obj in queryset:
            obj.outstanding_debt = 0.00
            obj.save()
        self.message_user(request, "Задолженность успешно очищена для выбранных объектов.")

    clear_outstanding_debt.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Factory)
class FactoryAdmin(NetworkNodeAdmin):
    pass


@admin.register(RetailNetwork)
class RetailNetworkAdmin(NetworkNodeAdmin):
    pass


@admin.register(Entrepreneur)
class EntrepreneurAdmin(NetworkNodeAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'node')

