from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'main',
        'name': 'Abhiseka Susanto',
        'class': 'C'
    }

    return render(request, "main.html", context)
