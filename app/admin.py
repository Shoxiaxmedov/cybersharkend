from django.contrib import admin
from app.models import *


admin.site.site_header = "Cyber Shark | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class DishAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','added_on','updated_on']

class PurchseAdmin(admin.ModelAdmin):
    list_display = ['id','user','time','name','item_count']

class ComandAdmin(admin.ModelAdmin):
    list_display = ['name', 'name2', 'name3', 'name4', 'name5', 'comandname']




admin.site.register(Contact, ContactAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Team, TeamAdmin )
admin.site.register(Dish, DishAdmin )

admin.site.register(Order)
admin.site.register(Comand)
admin.site.register(Purchase)
admin.site.register(Profile)



