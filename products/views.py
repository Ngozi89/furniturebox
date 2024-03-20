from django.shortcuts import render
from .models import Furniture

# Create your views here.
def all_furnitures(request):
    """ A view to show all furnitures, include sorting and search queries """

    products = Furniture.objects.all()

    context = {
        'products':products,
    }

    return render(request, 'products/furnitures.html', context)