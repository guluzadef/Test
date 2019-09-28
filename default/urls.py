from django.conf.urls import url
from .views import Home,add_food


urlpatterns = [
    url('', Home, name="home"),
    url('add/', add_food, name="add-food"),

]