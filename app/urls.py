from django.urls import path
from django.contrib import admin
from .views import index, details, full, email, download

urlpatterns = [
    path('', index, name='index'),
    path('all-projects', full, name='full'),
    path('details/<slug:slug>', details, name='detail'),
    path('email', email, name='email'),
    path('download/<slug:slug>', download, name='download'),

]

admin.site.site_header = 'E-Portfolio administration'
admin.site.index_title = 'E-Portfolio'
admin.site.site_title = 'Bakhtiyar Garashov'
