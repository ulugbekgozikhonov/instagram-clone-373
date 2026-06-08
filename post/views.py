from django.shortcuts import render

def post_list_view(request):
    return render(request, "index.html")

def post_detail_view(request, id):
    return render(request, "abuzar.html", {"id": id})