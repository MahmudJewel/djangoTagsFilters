from django.urls import path, include
from second import views

urlpatterns = [
    path('', views.home, name='home'),

    path('lower', views.lower, name='lower'),
    path('reference', views.reference, name='reference'),

]