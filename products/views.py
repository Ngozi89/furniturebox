from django.shortcuts import render, get_object_or_404
from .models import Furniture

# Create your views here.
def all_furnitures(request):
    """ A view to show all furnitures, include sorting and search queries """

    products = Furniture.objects.all()

    context = {
        'products':products,
    }

    return render(request, 'products/furnitures.html', context)

def furniture_detail(request, Furniture_id):
    """ A view to show individual furniture details """

    product = get_object_or_404(Furniture, pk=furniture_id)

    context = {
        'furniture': furniture,
    }

    return render(request, 'products/furniture_detail.html', context)    