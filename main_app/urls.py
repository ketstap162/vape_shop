from django.urls import path

from main_app.views import home_page_view

app_name = "MainApp"

urlpatterns = [
    path("", home_page_view, name="home")
]
