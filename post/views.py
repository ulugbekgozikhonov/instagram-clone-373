from django.shortcuts import render

def post_list_view(request):
    return render(request, "index.html")

def post_tesha_view(request):
    return render(request, "tesha.html")