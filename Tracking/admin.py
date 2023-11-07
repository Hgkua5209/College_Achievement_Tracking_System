from django.contrib import admin
from .models import Student
from .models import Advisor
from .models import SportsClubs
from .models import Achivement
from .models import MeritRequest

# Register your models here.

admin.site.register(Student)
admin.site.register(Advisor)
admin.site.register(SportsClubs)
admin.site.register(Achivement)
admin.site.register(MeritRequest)
