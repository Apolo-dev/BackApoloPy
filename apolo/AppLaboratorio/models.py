from django.db import models

# Create your models here.

class LabGiratorio(models.Model):
    peso1 = models.FloatField(blank=False, null=False)
    peso2 = models.FloatField(blank=False, null=False)
    peso3 = models.FloatField(blank=False, null=False)
    peso4 = models.FloatField(blank=False, null=False)
    peso5 = models.FloatField(blank=False, null=False)
    peso6 = models.FloatField(blank=False, null=False)
    peso7 = models.FloatField(blank=False, null=False)
    peso8 = models.FloatField(blank=False, null=False)
    peso9 = models.FloatField(blank=False, null=False)
    peso10 = models.FloatField(blank=False, null=False)
    peso11 = models.FloatField(blank=False, null=False)
    peso12 = models.FloatField(blank=False, null=False)
    peso13 = models.FloatField(blank=False, null=False)
    peso14 = models.FloatField(blank=False, null=False)
    peso15 = models.FloatField(blank=False, null=False)
    peso16 = models.FloatField(blank=False, null=False)
    peso17 = models.FloatField(blank=False, null=False)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Abertura(models.Model):
    
    abertura1 = models.IntegerField(blank=False, null=False)
    abertura2 = models.IntegerField(blank=False, null=False)
    abertura3 = models.IntegerField(blank=False, null=False)
    abertura4 = models.IntegerField(blank=False, null=False)
    abertura5 = models.IntegerField(blank=False, null=False)
    abertura6 = models.IntegerField(blank=False, null=False)
    abertura7 = models.IntegerField(blank=False, null=False)
    abertura8 = models.IntegerField(blank=False, null=False)
    abertura9 = models.IntegerField(blank=False, null=False)
    abertura10 = models.IntegerField(blank=False, null=False)
    abertura11 = models.IntegerField(blank=False, null=False)
    abertura12 = models.IntegerField(blank=False, null=False)
    abertura13 = models.IntegerField(blank=False, null=False)
    abertura14 = models.IntegerField(blank=False, null=False)
    abertura15 = models.IntegerField(blank=False, null=False)
    abertura16 = models.IntegerField(blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)





class Energia(models.Model):
    wi = models.PositiveIntegerField(blank=False, null=False)
    p80 = models.PositiveIntegerField(blank=False, null=False)
    f80 = models.PositiveIntegerField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["wi"]

    

    

    
