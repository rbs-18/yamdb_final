from django.contrib import admin

from .models import Genre, Category, Title, GenreTitle, Review, Comment


class TitleInline(admin.TabularInline):
    model = GenreTitle
    extra = 0


class TitleAdmin(admin.ModelAdmin):
    inlines = [TitleInline]
    list_display = (
        'pk',
        'name',
        'year',
    )


class GenreTitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'genre',
    )


admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Title, TitleAdmin)
admin.site.register(GenreTitle, GenreTitleAdmin)
admin.site.register(Review)
admin.site.register(Comment)
