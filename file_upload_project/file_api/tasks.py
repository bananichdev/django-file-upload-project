import os
from datetime import datetime
from celery import shared_task
from .models import File


@shared_task
def process_file(file_id):
    file_instance = File.objects.get(id=file_id)
    file_path = file_instance.file.path

    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    _, file_extension = os.path.splitext(file_path)

    new_file_name = f'{current_datetime}{file_extension}'
    file_directory = os.path.dirname(file_path)
    new_file_path = os.path.join(file_directory, new_file_name)

    os.rename(file_path, new_file_path)

    file_instance.processed = True
    file_instance.save()
