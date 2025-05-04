from django.db import models
from django.utils import timezone
from gsheets import mixins
# Create your models here.

class JobApplications(mixins.SheetSyncableMixin, models.Model):
    spreadsheet_id = 'YOUR_GOOGLE_SHEET_ID'
    STATUS_CHOICES = [
        ('NR', 'No response'),
        ('IV', 'Interview'),
        ('RJ', 'Rejected'),
        ('OF', 'Offer'),
        ('NA', 'N/A'),
    ]

    company_name = models.CharField(max_length=100)
    date_applied = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NA')
    position = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.company_name} - {self.position}"