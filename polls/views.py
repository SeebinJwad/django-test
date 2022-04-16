from django.http import HttpResponse

def index(requqest):
    return HttpResponse("Hello World")
