from django.urls import path, include

from .views import (
    landing_page
    
)

from . import views

urlpatterns = [
    # list the filed names, field desc, table name etc from metadata
    path('', landing_page),
 
]