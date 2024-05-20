from django.shortcuts import render
from django.http import JsonResponse
from .models import Data
from django.db.models import Sum, Avg


def home(request):
    data = Data.objects.all()
    context = {
        'data': data
    }
    context.values
    return render(request, 'base/home.html', context)

def get_data(request):
  data = Data.objects.all().values('end_year', 'intensity', 'sector')
  data_list = list(data)  
  return JsonResponse(data_list, safe=False)


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


