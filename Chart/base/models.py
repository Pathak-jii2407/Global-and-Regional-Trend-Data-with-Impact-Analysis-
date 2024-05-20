from django.db import models

class Data(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    end_year = models.FloatField(blank=True, null=True)
    intensity = models.FloatField()
    sector = models.CharField(max_length=255)
    topic = models.CharField(max_length=555)
    insight = models.TextField()
    url = models.URLField(max_length=500)
    region = models.CharField(max_length=255)
    start_year = models.FloatField(blank=True, null=True)
    impact = models.FloatField(blank=True, null=True)
    added = models.DateTimeField()
    published = models.DateTimeField()
    country = models.CharField(max_length=255)
    relevance = models.FloatField()
    pestle = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=524)
    likelihood = models.FloatField()

    def __str__(self):
        return f"{self.title} ({self.sector})"


