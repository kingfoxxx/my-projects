from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # This pattern matches the root URL and directs it to the dashboard view
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),  # Redirect favicon.ico requests
    # Other URL patterns...
]
