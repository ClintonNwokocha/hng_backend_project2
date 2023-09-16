from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Person
import json

@csrf_exempt
@api_view(['POST'])
def create_person(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        if name is None:
            return JsonResponse({'error': 'Name is required'}, status=400)
        
        person = Person.objects.create(name=name)
        return JsonResponse({'id': person.id, 'name': person.name})

    return JsonResponse({'error': 'This endpoint only supports POST requests'}, status=405)

@csrf_exempt
@api_view(['GET'])
def read_person(request, user_id):
    try:
        person = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        return JsonResponse({'error': 'Person not found'}, status=404)
    return JsonResponse({'id': person.id, 'name': person.name})

@csrf_exempt
@api_view(['PUT'])
def update_person(request, user_id):
    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        if name is None:
            return JsonResponse({'error': 'Name is required'}, status=400)
        
        try:
            person = Person.objects.get(id=user_id)
        except Person.DoesNotExist:
            return JsonResponse({'error': 'Person not found'}, status=404)

        person.name = name
        person.save()
        return JsonResponse({'id': person.id, 'name': person.name})

@csrf_exempt
@api_view(['DELETE'])
def delete_person(request, user_id):
    try:
        person = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        return JsonResponse({'error': 'Person not found'}, status=404)
    person.delete()
    return JsonResponse({'message': 'Person deleted successfully'})
