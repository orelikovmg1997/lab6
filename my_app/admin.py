from django.contrib import admin
from .models import User, Computer, Order

# Register your models here.

admin.site.register(User)
admin.site.register(Computer)
admin.site.register(Order)