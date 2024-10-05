from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

def vehicle_add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/vehicle_form.html', {'form': form})

def vehicle_detail(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    return render(request, 'vehicles/vehicle_detail.html', {'vehicle': vehicle})

def vehicle_list(request):
    query = request.GET.get('q')
    if query:
        vehicles = Vehicle.objects.filter(models.Q(make__icontains=query) | models.Q(model__icontains=query))
    else:
        vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})
