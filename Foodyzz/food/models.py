from django.db import models

# Create your models here.
# python manage.py migrate : It looks to all apps which are under the installed apps and create necessary database tables according to the database settings in setting.py file.

class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()