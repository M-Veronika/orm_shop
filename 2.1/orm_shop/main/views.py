from django.http import Http404
from django.shortcuts import get_object_or_404, render

from main.models import Car, Sale


def cars_list_view(request):
    cars = Car.objects.all() 
    template_name = 'main/list.html'
    return render(request, template_name, {'cars': cars})  # передайте необходимый контекст


def car_details_view(request,id_auto):
    car = get_object_or_404(Car, id=id_auto)
    template_name = 'main/details.html'
    return render(request, template_name, {'car': car})  # передайте необходимый контекст


def sales_by_car(request, id_auto):
    try:
        car = get_object_or_404(Car, id=id_auto)
        sales = Sale.objects.filter(car=car)                   # получите авто и его продажи
        template_name = 'main/sales.html'
        return render(request, template_name, {'car': car, 'sales': sales})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
