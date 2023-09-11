from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Person
from django.core.serializers import serialize
import json 

# Create your views here.

# Create Operation
def create_person(request):
    name = request.GET.get('name')
    if not name:
        return JsonResponse({'error': 'Name is required'}, status=400)
    
    person = Person.objects.create(name=name)
    return JsonResponse({'id': person.id, 'name': person.name})

# Read Operation
def read_person(request, user_id):
    try:
        person = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        return JsonResponse({'error': 'Person not found'}, status = 404)
    
    return JsonResponse({'id': person.id, 'name': person.name})

# Update Operation
def update_person(request, user_id):
    name = request.GET.get('name')
    if not name:
        return JsonResponse({'error': 'Name is required'}, status = 400)

    try:
        person = Person.objects.get(id=user_id)

    except Person.DoesNotExist:
        return JsonResponse({'error': 'Person not found'}, status = 404)
    
    person.name = name
    person.save()

    return JsonResponse({'id': person.id, 'name': person.name})

# Delete Operation
def delete_person(request, user_id):
    try:
        person = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        return JsonResponse({'error': 'Person no found'}, status=404)
    
    person.delete()
    return JsonResponse({'message': 'Person deleted'})
