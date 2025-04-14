from django.db import models
from django.conf import settings

from constructions.models import Construction


class Entry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    operational_activity = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    # Można dodać relację ManyToMany lub oddzielny model dla zdjęć, aby ograniczyć ich ilość

    def __str__(self):
        return f'{self.author.username} - {self.created_at}'
