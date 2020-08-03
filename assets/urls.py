from django.urls import path
from assets import views

app_name = 'assets'

urlpatterns = [
    path('report/', views.report, name='report'),
    path('detail/<int:asset_id>/', views.detail, name="detail"),
]
