from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def cars(requests):
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 4)
    page = requests.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    context = {
        'all_cars': paged_cars,
        'model_search': model_search,
        'state_search' : state_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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
    model_search = Car.objects.values_list('model', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()


    if 'keyword' in requests.GET:
        keyword = requests.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in requests.GET:
        model = requests.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    
    if 'state' in requests.GET:
        state = requests.GET['state']
        if state:
            cars = cars.filter(state__iexact=state)

    if 'year' in requests.GET:
        year = requests.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in requests.GET:
        body_style = requests.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in requests.GET:
        min_price = requests.GET['min_price']
        max_price = requests.GET['max_price']
        if max_price:
           cars = cars.filter(price__gte=min_price, price__lte=max_price)
    
    context = {
        'cars': cars,
        'model_search': model_search,
        'state_search' : state_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    return render(requests, 'cars/search.html', context)