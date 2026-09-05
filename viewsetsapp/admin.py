from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age', 'phone')
    search_fields = ('name', 'email')
    list_filter = ('age')