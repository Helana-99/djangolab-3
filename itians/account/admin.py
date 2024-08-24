from django.contrib import admin
from .models import Account  # Import the Account model

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
