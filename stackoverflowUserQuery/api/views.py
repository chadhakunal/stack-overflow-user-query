from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView


# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello World</h1>")


class TagPredictView(APIView):
    def get(self, request):
        response_data = {'result': 'error', 'message': 'Some error message'}
        return JsonResponse(response_data)

    def post(self, request):
        print(request.data)
        response_data = {'result': 'error', 'message': 'Some error message'}
        return JsonResponse(response_data)


class QueryPredictView(APIView):
    def get(self, request):
        response_data = {'result': 'error', 'message': 'Some error message'}
        return JsonResponse(response_data)

    def post(self, request):
        print(request.data)
        response_data = {'result': 'error', 'message': 'Some error message'}
        return JsonResponse(response_data)
