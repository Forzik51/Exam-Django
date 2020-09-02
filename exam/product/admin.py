from django.contrib import admin
from django.utils.html import format_html
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description',
                    'price', 'actions_', 'photo')
    list_display_links = ('id', 'name', 'short_description')
    list_editable = ('price',)
    save_as = True

    def short_description(self, obj):
        return obj.description[:100]+" ..." if len(obj.description) > 100 else obj.description
    short_description.short_description = 'description'

    def photo(self, obj):
        return format_html("<a href='/static/{}'><img style='max-width:30px; max-height:30px;' src='/static/{}'/></a>", obj.main_photo, obj.main_photo)

    def actions_(self, obj):
        return format_html("""<a style='display:inline-block; margin: 3px;' href='/admin/product/product/{}/change/'>
                                <input type='button' value='Edit'/>
                                </a>
                            <a style='display:inline-block; margin: 3px;' href='/admin/product/product/{}/delete/'>
                            <input type='button' value='Delete'/>
                            </a>
                            """, obj.id, obj.id)


admin.site.register(Product, ProductAdmin)
