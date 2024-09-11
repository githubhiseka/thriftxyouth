from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'THRIFTxYouth',
        'name': 'Abhiseka Susanto',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
