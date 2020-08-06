from django.contrib import admin
from .models import Post
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.apps import apps

class PostAdmin(admin.ModelAdmin): 
 list_display = ['author', 'title', 'text', 'created_date', 'published_date' ]
 list_filter = ('published_date', )
 
 def active(self, obj): 
        return obj.is_active == 1
  
 active.boolean = True

admin.site.register(Post, PostAdmin)