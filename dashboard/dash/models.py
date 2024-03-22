from django.db import models

class Dash(models.Model):
    end_year = models.IntegerField()
    intensity = models.IntegerField(null=True, blank=True)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.IntegerField(null=True, blank=True)
    impact = models.CharField(max_length=100, null=True, blank=True)
    added = models.DateTimeField()
    published = models.DateTimeField()
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likelihood = models.IntegerField()

    def __str__(self):
        return f"{self.intensity} - {self.likelihood} - {self.relevance} - {self.end_year} - {self.country} - {self.topic} - {self.region} - {self.impact}"
