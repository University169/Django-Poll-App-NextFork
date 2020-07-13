from django.contrib import admin
from .models import Poll, Choice, Vote, Questionnaire

admin.site.register(Questionnaire)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)
