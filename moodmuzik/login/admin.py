from django.contrib import admin

# Register your models here.
from .models import User,Session,Song

admin.site.register(User)
admin.site.register(Song)
admin.site.register(Session)