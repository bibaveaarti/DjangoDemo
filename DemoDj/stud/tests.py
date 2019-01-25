from django.test import TestCase

# Create your tests here.

class student(models.Model):
    def __str__(self):
        return self.name
