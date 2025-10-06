from django.db import models

# Create your models here.
    


class Notes(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField()
    pinned = models.BooleanField(default=False)
    color = models.TextField(default="indigo",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title