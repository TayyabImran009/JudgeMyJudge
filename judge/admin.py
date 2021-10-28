from django.contrib import admin
from .models import*
# Register your models here.

admin.site.register(judge)
admin.site.register(judgeRateing)
admin.site.register(bestInterest)

admin.site.register(categories)

admin.site.register(tags)

admin.site.register(judgeTags)
