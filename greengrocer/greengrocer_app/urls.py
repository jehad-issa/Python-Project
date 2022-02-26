from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('farmer', views.farmer),
    path('logout/',views.logout),
    path('farmer/add_crop',views.add_crop),
    path('new_crop',views.new_crop),
    path('farmer/edit_crop/<num>',views.edit_crop),
    path('edit_new_crop/<num>',views.new_edit_crop),
    path('delete/<num>',views.delete),
    path('trader', views.trader),
    path('trader/buy', views.trader_buy_crop),
    path('trader/purchases', views.purchases),
    
]