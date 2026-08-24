from django.db import models
class User(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name