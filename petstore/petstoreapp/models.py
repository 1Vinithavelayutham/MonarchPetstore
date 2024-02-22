from django.db import models

class PetStore(models.Model):
       Name =models.CharField(max_length=50)
       email=models.EmailField(max_length=50)
       mobile=models.BigIntegerField()
       Msg=models.CharField(max_length=200)
