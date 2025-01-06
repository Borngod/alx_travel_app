from django.urls import path
from . import views

app_name='alx_travel_app.listings'
urlpatterns = [
    path('',views.home_view)
]
