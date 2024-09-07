from django.contrib import admin

from order.models.menu import Menu
from order.models.category import Category
from order.models.item import Item
from order.models.modifier import  Modifier
from order.models.order import Order

# Register your models here.

admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Modifier)
admin.site.register(Order)





