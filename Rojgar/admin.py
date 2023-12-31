from django.contrib import admin
from .models import *
from Rojgar.models import user_request
# Register your models here.
admin.site.register(WorkerStat)
# Register your models here.
admin.site.register(user_request)
admin.site.register(UserData)
