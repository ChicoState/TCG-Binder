from django.contrib import admin
from .models import libraryEntry
    
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('deckID', 'cardIDs')
    
admin.site.register(libraryEntry, LibraryAdmin)