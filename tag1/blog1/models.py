from django.db import models
from datetime import datetime, date

# Create your models here.
class AbstractModel(models.Model):
    date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(AbstractModel):
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="help text")
    deleted = models.BooleanField(default=False)