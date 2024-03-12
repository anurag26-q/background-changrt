from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=300)
    item_desc=models.CharField(max_length=300)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default='https://www.treicamile.ro/wp-content/uploads/2021/11/food-placeholder.png')

    def __str__(self):
        return f"{self.item_name},{self.item_desc},{self.item_price}"
    class Meta:
        verbose_name=('Item name')
