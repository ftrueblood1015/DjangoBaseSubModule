from tabnanny import verbose
from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class BaseTrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()

    class Meta:
        verbose_name = f'VERBOSE NOT SET {__name__}'
        verbose_name_plural = f'VERBOSE PLURAL NOT SET {__name__}'
        abstract = True

    def __str__(self):
        return f'{self.description}'