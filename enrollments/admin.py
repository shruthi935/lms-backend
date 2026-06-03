from django.contrib import admin

# Register your models here.

from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "student",
        "course",
        "progress_percentage",
        "completed",
        "enrolled_at"
    )

    list_filter = (
        "completed",
    )

    search_fields = (
        "student__username",
        "course__title",
    )