from django.db import models

# Create your models here.

from courses.models import Course


class Lesson(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons"
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    video_url = models.URLField(
        blank=True,
        null=True
    )

    pdf_file = models.FileField(
        upload_to="lesson_pdfs/",
        blank=True,
        null=True
    )

    duration = models.IntegerField(
        default=0
    )

    order = models.PositiveIntegerField(
        default=1
    )

    is_free_preview = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title