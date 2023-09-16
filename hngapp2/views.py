from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Person
from django.core.serializers import serialize
import json 

# Create your views here.

@csrf_exempt
def create_person(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        name = data.get('name', None) 
        if not name:
            return JsonResponse({'error': 'Name is required'}, status=400)
        
        person = Person.objects.create(name=name)  
        return JsonResponse({'id': person.id, 'name': person.name})
    else:
        return JsonResponse({'error': 'This endpoint only supports POST requests.'}, status=400)


# Read Operation
def read_person(request, user_id):
    try:
        person = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        return JsonResponse({'error': 'Person not found'}, status = 404)
    
    return JsonResponse({'id': person.id, 'name': person.name})

# Update Operation
def update_person(request, user_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
            
        name = data.get('name', None)
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
