from django.db import models
from django_extensions.db.fields import ShortUUIDField


class Target(models.Model):
    """Targets define what is being scanned for vulnerabilities."""
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}"

class Definition(models.Model):
    """Definitions are the vulnerabilities that we are looking for."""
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True) # description

    def __str__(self):
        return f"{self.id}"

class Finding(models.Model):
    """Findings are security issues found during scans.
    Findings come with all the data we gathered during the scan, 
    a suggestion on how to fix it, and a description of the vulnerability.
    """
    target = models.ForeignKey(Target, on_delete=models.SET_NULL, null=True)
    definition = models.ForeignKey(Definition, on_delete=models.SET_NULL, null=True)
    scans = models.TextField() # Used to simplify the data structure
    url = models.URLField(blank=True)
    path = models.CharField(max_length=255, blank=True)
    method = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.id}"