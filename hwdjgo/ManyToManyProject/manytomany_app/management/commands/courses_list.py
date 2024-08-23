from django.core.management.base import BaseCommand
from manytomany_app.models import Course

class Command(BaseCommand):
    def handle(self, *args, **options):
        courses = Course.objects.all()
        return courses