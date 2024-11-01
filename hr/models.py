import uuid
from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.phone

class Employee(models.Model):
    class Workplace(models.IntegerChoices):
        JOB_1 = 1, "Junior"
        JOB_2 = 2, "Middle"
        JOB_3 = 3, "Senior"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    workspace = models.PositiveSmallIntegerField(
        choices=Workplace.choices,
        default=Workplace.JOB_1,
        help_text="Choose your workplace",
    )
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name
