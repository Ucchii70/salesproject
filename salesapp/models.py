from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
                       
class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    progress = models.IntegerField(choices=[(0, "電話連絡済み"),(1, "訪問済み"),(2, "契約書送付済み"),(3, "契約済み"),(4, "失注")])
    manager_checked = models.BooleanField(default=False)
    memo = models.TextField()
    staff = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={"is_superuser":False})

    def __str__(self):
        return self.customer.name