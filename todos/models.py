from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField("Title", max_length=100)
    complete = models.BooleanField("Is completed", default=False)
    create_at = models.DateTimeField("Created at", auto_now_add=True)
    update_at = models.DateTimeField("Created at", auto_now=True)

    def __str__(self) -> str:
        return f"({'+' if self.complete else '-'}) {self.title} {self.create_at} {self.update_at}"

