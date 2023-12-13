from django.db import models
import uuid


class ConcernLevel(models.Model):
    school = models.CharField(max_length=20)
    speciality = models.CharField(max_length=20)
    faculty = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    campus = models.CharField(max_length=20)

class Information(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('unvalid', 'Unvalid'),
        ('pending', 'Pending'),
    ]
       
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices= STATUS_CHOICES,)
    concern_levels = models.ManyToManyField(ConcernLevel)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title
