from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax_rate=0.15
def index(request):
    return render(request, "program/index.html")
def taxrate(request):
    return render(request, "program/tax.html", {"taxrate":tax_rate})
def anynumber(request, name):
    return HttpResponse(f"The total price after taxrate is : {int(name)*tax_rate+int(name)}")
