from django.db import models

# Create your models here.
class turbidity(models.Model):
    turbidity_value=models.IntegerField(default=0)
    time=models.DateTimeField('Date accesed')

    def __str__(self):
        return str(self.turbidity_value)

