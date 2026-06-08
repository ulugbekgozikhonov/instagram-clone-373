from django.shortcuts import render

def post_list_view(request):
    return render(request, "index.html")
