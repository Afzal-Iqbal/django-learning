from django.urls import path
from . import views

# localhost:8000/simosa
# localhost:8000/simosa/order
urlpatterns = [
    path('', views.all_simosa, name='all_simosa'),
    # path('order/', views.order, name='order'),
]