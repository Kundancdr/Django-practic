from django.db import models

class Employee(models.Model) :
    e_no = models.IntegerField()
    e_name = models.CharField(max_length = 30)
    e_sal = models.FloatField()
    def __str__(self):
        return self.e_name