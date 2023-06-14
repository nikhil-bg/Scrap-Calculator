from django.db import models

class ScrapProduct(models.Model):
    component_length = models.FloatField()
    component_weight = models.FloatField()
    rod_weight = models.FloatField()
    rod_length = models.FloatField()
    scrap_value = models.FloatField(null=True)
