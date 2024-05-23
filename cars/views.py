from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def cars(requests):
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 4)
    page = requests.GET.get('page')
    paged_cars = paginator.get_page(page)
    context = {
        'all_cars': paged_cars,
    }
    return render(requests, 'cars/cars.html', context)

def car_detail(requests, id):
    single_car = get_object_or_404(Car, pk=id)
    context = {
        'single_car': single_car,
    }
    return render(requests, 'cars/car_detail.html', context)

def search(requests):
    cars = Car.objects.order_by('-created_date')
    if 'keyword' in requests.GET:
        keyword = requests.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
    context = {
        'cars': cars,
    }
    return render(requests, 'cars/search.html', context)