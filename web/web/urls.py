from django.contrib import admin
from django.urls import path
admin.site.site_header = 'Яндекс практикум'
urlpatterns = [
    path('admin/', admin.site.urls),
]
