from django.shortcuts import render
from .models import Item


# Create your views here.
def name_list(request):
    names = Item.objects.all()
    print(names)
    return render(request, 'simple_app/name_list.html', {'names': names})
