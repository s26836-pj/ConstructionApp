from django.db import models


class Construction(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    working_hours = models.CharField(max_length=20)  # e.g., "08:00-17:00"
    is_archived = models.BooleanField(default=False)
    archive_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
