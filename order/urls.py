from django.urls import path
from order.views.get_component import (menu_list,
                                       category_list,
                                       item_list,
                                       modifier_list)


from order.views.create_component import (
                                        create_menu,
                                        create_category,
                                        create_item,
                                        create_modifier)

from order.views.place_order import place_order

urlpatterns = [
    #----------------------------get
    path('menus/', menu_list, name='menu-list'),
    path('categories/', category_list, name='category-list'),
    path('items/', item_list, name='item-list'),
    path('modifiers/', modifier_list, name='modifier-list'),
    
    #----------------------------create
    
    path('menus/create/', create_menu, name='create-menu'),
    path('categories/create/', create_category, name='create-category'),
    path('items/create/', create_item, name='create-item'),
    path('modifiers/create/', create_modifier, name='create-modifier'),
    
    #---------------payment
    path('orders/place/', place_order, name='place-order'),
]
