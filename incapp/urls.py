from django.urls import path
from incapp import views

urlpatterns = [
    path(route="", view=views.view_data, name="view_data"),
]
