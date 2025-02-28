from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Helm Charts Post</h1><p>Homepage</p>")
