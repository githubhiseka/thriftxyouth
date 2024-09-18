from django.db import models
import uuid

class Product(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	description = models.TextField()

# untuk demo tugas 2
class Person(models.Model):
	name = models.CharField(max_length=255)
	age = models.IntegerField()
	is_happy = models.BooleanField()