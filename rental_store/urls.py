from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("rental_store", views.rental_store, name="rental-store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    path("process_order/", views.processOrder, name="process_order"),
    path("about/", views.about, name="about"),
    path("map/",views.map_view, name="map")

]