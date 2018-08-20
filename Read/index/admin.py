from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(UserInfo)
admin.site.register(content)
admin.site.register(Commit)