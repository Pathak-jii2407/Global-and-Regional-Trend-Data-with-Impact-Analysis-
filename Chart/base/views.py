from django.shortcuts import render
from django.http import JsonResponse
from .models import Data,Subscribe
from django.db.models import Sum, Avg
from django.shortcuts import render, redirect


def home(request):
    data = Data.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'base/home.html', context)

def get_data(request):
  data = Data.objects.all().values()
  values = {'data':data}
  return render(request,'base/get_all_data.html',values)
# views.py



def brief_detail_view(request, detail_id):
    detail_object = Data.objects.get(id=detail_id)
    return render(request, 'base/brief-detail.html', {'detail_object': detail_object})


def get_pie_chart(request):
    data = list(Data.objects.values('sector').annotate(
        total_intensity=Sum('intensity'), 
        avg_intensity=Avg('intensity')
    ))
    return JsonResponse(data, safe=False)


def pie_chart(request):
    return render(request, 'base/pie_chart.html') 


def get_intensity_by_sector(request):
    intensity_data = Data.objects.values('sector').annotate(total_intensity=Sum('intensity'))
    return JsonResponse(list(intensity_data), safe=False)

def intensity_by_sector(request):
    return render(request, 'base/intensity_by_sector.html')


def get_relevance_by_country(request):
    relevance_data = Data.objects.values('country').annotate(relevance=Avg('relevance'))
    return JsonResponse(list(relevance_data), safe=False)

def relevance_by_country(request):
    return render(request, 'base/relevance_by_country.html')


def get_likelihood_by_sector(request):
    likelihood_data = Data.objects.values('sector').annotate(likelihood=Avg('likelihood'))
    return JsonResponse(list(likelihood_data), safe=False)

def likelihood_by_sector(request):
    return render(request, 'base/likelihood_by_sector.html')



def get_impact_by_region(request):
    impact_data = Data.objects.values('region').annotate(impact=Avg('impact'))
    return JsonResponse(list(impact_data), safe=False)

def impact_by_region(request):
    return render(request, 'base/impact_by_region.html')



def get_trends_over_years(request):
    trends_data = Data.objects.values('start_year', 'end_year').annotate(
        intensity=Avg('intensity'),
        impact=Avg('impact'),
        relevance=Avg('relevance'),
    )
    return JsonResponse(list(trends_data), safe=False)

def trends_over_years(request):
    return render(request, 'base/trends_over_years.html')

def subscribe(request):
    return render(request, 'base/home.html')



from django.shortcuts import render, redirect
from .models import Subscribe

def subscribe(request):
    email=None
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if Subscribe.objects.filter(email=email).exists():  
                pass
            else:
                Subscribe.objects.create(email=email)
        return redirect('subscribe')
    
    subscribers = Subscribe.objects.all()
    subscriber_count = subscribers.count()
   
    params={'subscriber_count': subscriber_count, 'subscribers': subscribers,
            'name':get_name(email)}
    
    return render(request, 'base/home.html', params)


def get_name(email):
    name_=''
    email=str(email)
    for name in email:
        if name>='A' or name>='a' and name>='Z' or name>='z' :
            name_+=name
        name_=name_.replace('gmailcom',' ')
    return name_.capitalize()
