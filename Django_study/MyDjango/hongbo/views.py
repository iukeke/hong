from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def hello(request) :
    res ={"code":"200",
        "msg":"success",
        "data":"[]"}
    # return HttpResponse("res")
    return JsonResponse(res)
