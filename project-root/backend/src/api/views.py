import pandas as pd
from django.http import JsonResponse

from .algorithms.room_allocation import allocate_rooms
from .csv_handling.csv_reader import read_csv_file

def upload_csv_files(request):
    if request.method == 'POST' and request.FILES['group_file'] and request.FILES['hostel_file']:
        group_file = request.FILES['group_file']
        hostel_file = request.FILES['hostel_file']

        group_data = read_csv_file(group_file)
        hostel_data = read_csv_file(hostel_file)

        allocation_result = allocate_rooms(group_data, hostel_data)

        return JsonResponse(allocation_result, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)