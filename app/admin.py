from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Post)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id','topic_name',)
admin.site.register(Topic, TopicAdmin)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('id','topic','content',)
admin.site.register(Content, ContentAdmin)

class ExampleAdmin(admin.ModelAdmin):
    list_display = ('id','topic','example',)
admin.site.register(Example, ExampleAdmin)