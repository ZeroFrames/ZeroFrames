from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('button',views.button),
    path('paint',views.paint)
]