from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('open', 'Open'),
        ('fixed', 'Fixed'),
        ('rejected', 'Rejected'),
        ('reopen', 'Reopen'),
        ('closed', 'Closed'),
        ('test_passed', 'Test Passed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

