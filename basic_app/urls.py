from django.urls import path
from basic_app import views

# For Template Tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name="relative"),
    path('other/', views.other, name="other"),
    path('', views.index, name="index")
]
