from django.db import models


class Wbs(models.Model):
    code = models.CharField(max_length=5,primary_key=True)
    description = models.CharField(max_length=50)
    equipment_type = models.CharField(max_length=20,null=True)

    def __str__(self):
        return str(self.code)

class Equipment_Type(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.type)

