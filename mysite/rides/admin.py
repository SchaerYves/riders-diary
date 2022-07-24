from django.contrib import admin

from .models import Activity, Athlete, Choice, Question
from .models import Question

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Athlete)
admin.site.register(Activity)
# Register your models here.
