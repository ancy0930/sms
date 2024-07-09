from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    TEACHER = "teacher"
    STUDENT = "student"
    ROLE_CHOICES = [
        (TEACHER, "Teacher"),
        (STUDENT, "Student"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_set_permissions", blank=True
    )

    def __str__(self):
        return self.username


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mark(models.Model):
    student = models.ForeignKey(
        User, limit_choices_to={"role": "student"}, on_delete=models.CASCADE
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()

    def __str__(self):
        return f"{self.student.username} - {self.subject.name}: {self.marks_obtained}"
