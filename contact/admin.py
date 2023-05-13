from django.contrib import admin
from contact.models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', )
    ordering = ('-id', )
    search_fields = ('id', 'first_name', 'last_name', 'phone', )
    list_per_page = 2
    list_max_show_all = 200
    list_display_links = ('id', 'first_name', 'phone', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id', )
