from django.db import models

class add_page(models.Model):
    title = models.CharField(max_length=200)
    completed_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    project_details = models.CharField(max_length=100)
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('contacted', 'Pass/Contected'),
    ]
    status = models.CharField(max_length=50 , choices=STATUS_CHOICES , default="pending")