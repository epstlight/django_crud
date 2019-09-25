from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from faker import Faker
import requests

def image_find(job_name):
    url = 'http://api.giphy.com/v1/gifs/search?api_key=RTn8tGS0AfjlEqgAXMCOQJGt54wzH0uO&q'
    data = requests.get(f'{url}={job_name}').json()
    picture = data['data'][0]['images']['fixed_width']['url']
    return picture


def search(request):
    return render(request, 'jobs/search.html')


def past_job(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        jobs = Job.objects.all()
        # for job in jobs:
        #     if job.name == name:
        #         context = {'job':job, 'picture': image_find(job.past_job)}
        #         return render(request, 'jobs/past_job.html', context)
        fake = Faker('')
        job = Job(name=name, past_job=fake.job(), profile_image=image)
        job.save()
        context = {'job':job, 'picture': image_find(job.past_job)}
        return render(request, 'jobs/past_job.html', context)
    else:
        return redirect('jobs:search')
# Create your views here.
