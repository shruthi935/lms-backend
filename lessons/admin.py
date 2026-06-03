from django.contrib import admin

# Register your models here.

from .models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "course",
        "duration",
        "order",
        "is_free_preview",
    )

    list_filter = (
        "course",
        "is_free_preview",
    )

    search_fields = (
        "title",
    )