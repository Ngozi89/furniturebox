from django.contrib import admin
from .models import Furniture, Category, Color

# Register your models here.
class FurnitureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'itemnumber',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('itemnumber',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ColorAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
