from django.shortcuts import render
from django.http import JsonResponse

def studentsView(request):
    students = {
        'id': 1,
        'name': 'John Doe',
        'age': 20,
    }
    return JsonResponse(students)