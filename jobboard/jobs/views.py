from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
import requests
from bs4 import BeautifulSoup

@api_view(['GET'])
def get_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def scrape_jobs(request):
    keyword = request.data.get('keyword', 'Product Manager')
    url = f"https://www.naukri.com/{keyword.replace(' ', '-')}-jobs"

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = soup.find_all('div', class_='jobTuple')  # Adjust selector as per website
    for job in job_listings:
        title = job.find('a', class_='title').text.strip()
        company = job.find('a', class_='subTitle').text.strip()
        location = job.find('li', class_='location').text.strip()
        experience = job.find('li', class_='exp').text.strip() if job.find('li', class_='exp') else "Not mentioned"
        link = job.find('a', class_='title')['href']

        Job.objects.create(title=title, company=company, location=location, experience=experience, application_link=link)

    return Response({'message': 'Jobs scraped successfully!'})


@api_view(['GET'])
def api_root(request):
    return Response({
        "jobs": "/api/jobs/",
        "scrape": "/api/scrape/"
    })