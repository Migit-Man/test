from django.db import models

# Create your models here.
class Announcement(models.Model):

    CATEGORIES = [
        ('MilitaryRP', 'MilitaryRP'),
        ('Discord', 'Discord'),
        ('Website', 'Website'),
        ('Community', 'Community'),
    ]

    date = models.DateTimeField(verbose_name="Published Date", auto_now=True)
    # slug = models.SlugField()
    title = models.CharField(max_length=40, verbose_name="Announcement Title")
    category = models.CharField(max_length=12, choices=CATEGORIES, default='MRP')
    description = models.TextField(verbose_name="Announcement Description")
    

    def __str__(self):
        return '[' + self.category + '] - ' + self.title

