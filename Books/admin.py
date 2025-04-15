from django.contrib import admin
from .models import Author, Publication, Book, PublicationsAuthor
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","year_of_birth")
    list_filter=("last_name","year_of_birth")
    def __str__(self):
       return self.first_name+" "+self.last_name
    
    def has_add_permission(self,request,obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_change_permisiion(self,request,obj=None):
        return False
    def has_delete_permisiion(self,request,obj=None):
        return False

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display=("title","author")

admin.site.register(Book, BookAdmin)

class PublicationAuthorAdmin(admin.StackedInline):
    model=PublicationsAuthor
    extra=0
    list_display=("author","publication")


class PublicationAdmin(admin.ModelAdmin):
    inlines=[PublicationAuthorAdmin]
    list_display=("name","address")

admin.site.register(Publication, PublicationAdmin)




