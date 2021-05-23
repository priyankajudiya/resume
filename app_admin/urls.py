from django.urls import path
from . import views
urlpatterns = [
    path('', views.admin.as_view(), name="myadmin"),
    path('saveProfile/<int:uid>', views.saveProfile.as_view(), name="saveProfile"),
]
