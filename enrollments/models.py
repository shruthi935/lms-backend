from django.db import models

# Create your models here.

from users.models import User
from courses.models import Course


class Enrollment(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    enrolled_at = models.DateTimeField(
        auto_now_add=True
    )

    completed = models.BooleanField(
        default=False
    )

    progress_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    class Meta:
        unique_together = (
            "student",
            "course"
        )

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"