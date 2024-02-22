from django import views
from django.contrib import admin
from django.urls import path
from petstoreapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/",views.create),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete/<rid>',views.delete),
    #path('edit/<rid>',views.edit),
    path('update/<id>', views.update, name='updaterecord'),
]