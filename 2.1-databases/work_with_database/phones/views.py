from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Phone

def catalog(request):
    phones = Phone.objects.all()
    sort_param = request.GET.get('sort', 'name')
    
    if sort_param == 'name':
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')
    elif sort_param == 'max_price':
        phones = phones.order_by('-price')
    
    return render(request, 'catalog.html', {
        'phones': phones,
        'current_sort': sort_param
    })

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})

def index(request):
    return redirect('catalog') 