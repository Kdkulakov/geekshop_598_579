from django.shortcuts import render


def products(request):
    links_menu = {'links': [
            {'href': 'products:index', 'name': 'все'},
            {'href': 'products:index', 'name': 'дом'},
            {'href': 'products:index', 'name': 'офис'},
            {'href': 'products:index', 'name': 'модерн'},
            {'href': 'products:index', 'name': 'классика'}
        ]}
    return render(request, 'products.html', context=links_menu)

