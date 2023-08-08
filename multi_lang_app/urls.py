# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    # URL for changing the language preference
    path('set_language/<str:language_code>/', views.set_language, name='set_language'),
]

