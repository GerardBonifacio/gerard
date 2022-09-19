from django.contrib import admin
from django.urls importh path

from .views import home_page

urlpatters= [
    path('', home_page),
    path('admin/', admin.site.urls),

]