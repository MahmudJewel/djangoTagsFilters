from django.urls import path, include
from second import views

urlpatterns = [
    path('', views.home, name='home'),

    path('string', views.string, name='string'),
    path('reference', views.reference, name='reference'),

    path('operation', views.operation, name='operation'),

]