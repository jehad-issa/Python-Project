from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('farmer', views.farmer),
    path('farmer/add_crop',views.add_crop),
    path('farmer/edit_crop/1',views.edit_crop),
    path('trader', views.trader),
    path('trader/buy', views.trader_buy_crop),
    path('trader/purchases', views.purchases),
]