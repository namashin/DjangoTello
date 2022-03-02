from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # これらの関数ベースビュー書いていく
    path('controller/', views.controller, name='controller'),
    path('api/command', views.command, name='command'),
]
