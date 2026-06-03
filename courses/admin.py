from django.contrib import admin

# Register your models here.

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "instructor",
        "price",
        "is_published"
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "category",
        "is_published",
    )