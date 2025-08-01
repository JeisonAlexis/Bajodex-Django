from django.shortcuts import render
from applications.babosas.models import babosas
from django.core.paginator import Paginator

def index(request):
    filtro  = request.GET.get('elemento')
    search  = request.GET.get('search', '').strip().lower()
    qs      = babosas.objects.all().order_by('codigoBabosa')

    if filtro:
        codigo = next((c for c, label in babosas.elemento
                       if label.lower() == filtro.lower()), None)
        if codigo:
            qs = qs.filter(elementoBabosa=codigo)

    tipo_dict = {
        'malvada': '1',
        'elemental': '2',
        'megamorfica': '3',
        'guardiana': '4',
        'extra': '5',
    }

    search_key = search[:-1] if search.endswith('s') else search
    tipo_codigo = tipo_dict.get(search_key)

    if search:
        if tipo_codigo:
            qs = qs.filter(tipoBabosa=tipo_codigo)
        elif search.isdigit():
            qs = qs.filter(codigoBabosa__regex=rf'^0*{search}$')
        else:
            qs = qs.filter(NombreBabosa__icontains=search)

    per_page = qs.count() or 1 if (filtro or search) else 16
    paginator = Paginator(qs, per_page)
    page_obj  = paginator.get_page(request.GET.get('page'))

    return render(request, 'home/index.html', {
        'page_obj': page_obj,
        'babosas': page_obj.object_list,
        'selected': filtro or ''
    })
