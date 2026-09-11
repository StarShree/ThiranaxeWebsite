from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_submit, name='contact_submit'),
    path('api/projects/<int:project_id>/', views.api_project_detail, name='project_detail_api'),
]
