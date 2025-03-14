from django.urls import path
from jobs.views import get_jobs, scrape_jobs

urlpatterns = [
    path('api/jobs/', get_jobs, name='get_jobs'),
    path('api/scrape/', scrape_jobs, name='scrape_jobs'),
]
