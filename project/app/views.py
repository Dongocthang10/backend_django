from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {"title": "Hello"}
    return render(request, "index.html", context)