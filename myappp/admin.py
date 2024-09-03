from django.contrib import admin
from .models import Blog,Contact

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description','date']
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Email','Subject','Message']
    

