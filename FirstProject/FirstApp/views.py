from django.shortcuts import render
from django.http import HttpResponse
exit


# Create your views here.
def index(request):
    return render(request, 'FirstApp/index.html')


def training_domain(request, domain_id):
    return HttpResponse("You are in the %s: " % domain_id)


def candidate(request, domain_id):
    response = "You are the candidate named as %s ."
    return HttpResponse(response % domain_id)

# def data(request):
#     return HttpResponse("Hello Customer !!! Please verify the data before proceeding")
# def worklist(request):
#     return HttpResponse("Hello Customer !!! Welcome to the worklist page . Please find the list of orders ")
# def forms(request):
#     return HttpResponse("Hello Customer !!! Please find the optional forms here if required ")
