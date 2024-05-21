from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_data/', views.get_data, name='get_data'),
    path('get_data/brief-detail/<int:detail_id>/', views.brief_detail_view, name='brief_detail'),
    path('get_pie_chart/', views.get_pie_chart, name='get_pie_chart'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
    path('get_intensity_by_sector/', views.get_intensity_by_sector, name='get_intensity_by_sector'),
    path('get_relevance_by_country/', views.get_relevance_by_country, name='get_relevance_by_country'),
    path('get_likelihood_by_sector/', views.get_likelihood_by_sector, name='get_likelihood_by_sector'),
    path('get_impact_by_region/', views.get_impact_by_region, name='get_impact_by_region'),
    path('intensity_by_sector/', views.intensity_by_sector, name='intensity_by_sector'),
    path('relevance_by_country/', views.relevance_by_country, name='relevance_by_country'),
    path('likelihood_by_sector/', views.likelihood_by_sector, name='likelihood_by_sector'),
    path('impact_by_region/', views.impact_by_region, name='impact_by_region'),
    path('get_trends_over_years/', views.get_trends_over_years, name='get_trends_over_years'),
    path('trends_over_years/', views.trends_over_years, name='trends_over_years'),
    path('subscribe', views.subscribe, name='subscribe'),


]
