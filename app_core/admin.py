from django.contrib import admin
from app_core import models

# Register your models here.

@admin.register(models.profile)
class profileAdminModel(admin.ModelAdmin):
    list_display = ['pk','name', 'lname', 'age', 'pic' ]

@admin.register(models.education)
class educationAdminModel(admin.ModelAdmin):
    list_display = ['pk', 'eduFor_id', 'eduFor', 'eduTitle', 'eduFrom', 'eduYear', 'eduDesc']

@admin.register(models.skils)
class skilsAdminModel(admin.ModelAdmin):
    list_display = ['pk', 'skilFor', 'skilTitle', 'skilPer']

@admin.register(models.knowledge)
class knowledgeAdminModel(admin.ModelAdmin):
    list_display = ['pk','knoFor_id','knoFor', 'knowledges']

@admin.register(models.experience)
class experienceAdminModel(admin.ModelAdmin):
    list_display = ['pk', 'expFor', 'title', 'compuny', 'fromDate', 'toDate', 'desc']

@admin.register(models.portfolio)
class portfolioAdminModel(admin.ModelAdmin):
    list_display = ['pk','portFor_id','portFor','title','img','url', 'date']

@admin.register(models.contact)
class contactAdminModel(admin.ModelAdmin):
    list_display =['messageFor', 'fullName', 'subject', 'email', 'message']