from django.contrib import admin
from .models import Person,loginperson


class PersonAdmin(admin.ModelAdmin):
  list_display = ("firstname","lastname","phone","email","date", "password")

class loginperrsonAdmin(admin.ModelAdmin):
  listdisplay1 = ("email","password")

admin.site.login(loginperson,loginperrsonAdmin)
admin.site.register(Person, PersonAdmin)
