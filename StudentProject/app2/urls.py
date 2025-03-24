from django.urls import path
from .views import sample

urlpatterns = [
    path('', sample, name='sample'),  # URL route for the 'sample' view
]