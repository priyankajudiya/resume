from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<int:pk>', views.portfolio.as_view(), name='portfolio'),
    path('contact', views.contact.as_view(), name='contact'),
]
