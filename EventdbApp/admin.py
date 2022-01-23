from django.contrib import admin

# Register your models here.

from .models import Winner, Prize, Location, Rules, Events

class EventsAdmin(admin.ModelAdmin):
    list_display = ('main_title', 'date', 'venue')
    prepopulated_fields = {'slug':('main_title',)}

admin.site.register(Events, EventsAdmin)
admin.site.register(Winner)
admin.site.register(Prize)
admin.site.register(Location)
admin.site.register(Rules)


