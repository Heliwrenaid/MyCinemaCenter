from django.contrib import admin

# Register your models here.
from .models import *

class Moderator(admin.ModelAdmin):
    readonly_fields = ['moderator', 'total_rating', 'opinion_counter', 'author', 'subscribed_by']

    def save_model(self, request, obj, form, change):
        if form.changed_data:
            obj.moderator = request.user.username
        super().save_model(request, obj, form, change)


admin.site.register(FilmOpinions)
admin.site.register(News)
admin.site.register(NewsOpinions)
admin.site.register(Film)
admin.site.register(Staff)
admin.site.register(Cinema, Moderator)
