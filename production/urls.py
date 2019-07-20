from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="index"),
    path ('catalog', views.index, name="catalog"),
    path ('detail', views.detail, name="detail"),

    path ('test', views.test, name="test"),
    path ('contact', views.contact, name="contact"),
    path ('contactme', views.contact, name="contactme")

]