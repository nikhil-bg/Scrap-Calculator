from django.shortcuts import render
from .models import ScrapProduct

def calculate_scrap(request):
    if request.method == 'POST':
        component_length = float(request.POST.get('component_length'))
        component_weight = float(request.POST.get('component_weight'))
        rod_weight = float(request.POST.get('rod_weight'))
        rod_length = float(request.POST.get('rod_length'))
        end_bit=float(request.POST.get('end_bit'))

        component_length += 2
        gram_weight = component_weight * 1000
        usable_rod = rod_length - end_bit
        parts_produced = usable_rod / component_length
        makeable_weight = gram_weight * parts_produced
        makeable_kg = makeable_weight / 1000
        scrap_value = round(rod_weight - makeable_kg)

        scrap_product = ScrapProduct.objects.create(
            component_length=component_length,
            component_weight=component_weight,
            rod_weight=rod_weight,
            rod_length=rod_length,
            scrap_value=scrap_value
        )
        scrap_product.save()

        return render(request, 'myapp/results.html', {'scrap_product': scrap_product})
    else:
        return render(request, 'myapp/calculate.html')
