from django.core.management.base import BaseCommand
from manytomany_app.models import Student

class Command(BaseCommand):
    def handle(self, *args, **options):
        students = Student.objects.all()
        return students