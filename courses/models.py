from django.db import models

# Create your models here.
from users.models import User
from categories.models import Category


class Course(models.Model):

    LEVEL_CHOICES = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    )

    title = models.CharField(
        max_length=255
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    description = models.TextField()
    thumbnail = models.ImageField(upload_to='courses/', null=True, blank=True)
    



    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="beginner"
    )

    duration = models.IntegerField(
        default=0
    )

    is_published = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title