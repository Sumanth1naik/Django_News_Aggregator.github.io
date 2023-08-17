from apihandler import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('news',views.index,name='index'),
]
