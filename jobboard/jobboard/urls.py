from django.urls import path
from jobs.views import get_jobs, scrape_jobs,api_root

urlpatterns = [
    path('', api_root, name='api_root'),  # Add this for the root URL
    path('api/jobs/', get_jobs, name='get_jobs'),
    path('api/scrape/', scrape_jobs, name='scrape_jobs'),
]