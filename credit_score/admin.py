from django.contrib import admin
from .models import Question,UserResponse,CreditScore

# Register your models here.

admin.site.register(Question)
admin.site.register(UserResponse)
admin.site.register(CreditScore)