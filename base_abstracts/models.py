from django.db import models
import uuid

# Create your models here.
class BaseModel:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class BaseTrackingModel:
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()

    class Meta:
        abstract = True