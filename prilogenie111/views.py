from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    response = render(request, 'prilogenie111/main_page.html', {})
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

def qqq(request):
    return HttpResponse(str("maxim"))

def qqq111(request):
    a = request.GET['a']
    b = request.GET['b']
    s = str(a) + str(b)
    print("Query_111: " + a + " " + b + " " + s)
    response = HttpResponse(str(s))
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

def qqq222(request):
    a = request.GET['a']
    b = request.GET['b']
    s = str(a) + str(b)
    print("Query_222: " + a + " " + b + " " + s)
    response = HttpResponse(str(s))
    response['Cache-Control'] = 'max-age=120'
    return response

