from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from tags.models import TaggedItem
from . import models
from .models import OrderItem


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset=None):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=20)


class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    autocomplete_fields = ['collection']
    list_display = ('title', 'unit_price', 'inventory', 'inventory_status', 'collection', 'collection_title')
    list_editable = ('unit_price',)
    list_per_page = 10
    list_select_related = ('collection',)
    list_filter = ('collection', 'last_updated', InventoryFilter)
    actions = ['clear_inventory']
    search_fields = ['title']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "Ok"

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated = queryset.update(inventory=0)  # خروجی تعداد رکورد های اپدیت شده ست
        self.message_user(
            request,
            f'inventory cleared for {updated}'
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'membership')
    list_editable = ('membership',)
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith', 'membership']
    list_per_page = 10


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_count')
    search_fields = ['title']

    @admin.display(ordering='product_count')
    def product_count(self, obj):
        url = (
                reverse('admin:store_product_changelist')
                + '?'
                + urlencode({'collection_id': str(obj.id)})
        )
        return format_html('<a href="{}">{}</a>', url, obj.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('product'))


class OrderItemInline(admin.StackedInline):
    autocomplete_fields = ['product']
    extra = 0
    min_num = 1
    max_num = 10
    model = OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ('id', 'placed_at', 'customer')
