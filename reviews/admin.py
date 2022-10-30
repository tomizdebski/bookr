from django.contrib import admin
from django.contrib.admin import AdminSite
from reviews.models import Publisher, Contributor, Book, BookContributor, Review


class BookrAdminSite(AdminSite):
    title_header = 'Aplikacja administracyjna Bookr'
    site_header = 'Aplikacja administracyjna Bookr'
    index_title = 'Administracja witryną Bookr'


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name__startswith')



admin_site = BookrAdminSite(name='bookr')

admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
