from django.db import models

category_choices = (
    ('All','All'),
    ('Juniors','Juniors'),
    ('Adults','Adults'),
)

class Product(models.Model):
    make = models.CharField(max_length=254, default='')
    """ No default product will be added into the database """
    category = models.CharField(max_length=254, choices=category_choices, default='')
    """ Category choices include view all, juniors and adults """
    juniors = models.CharField(max_length=50, default=True)
    """ Junior rugby players """
    adults = models.CharField(max_length=50, default=True)
    """ Adult rugby players """
    size = models.IntegerField()
    """ Size of the product """
    colour = models.CharField(max_length=50)
    """ Product colour """
    studs = models.CharField(max_length=50)
    """ Stud configuration of boot. Either moulded or screwin """
    quality = models.CharField(max_length=50, null=True)
    """ Brand new, almost new and general wear """ 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    """ Pricing model will be less than £1m and decimal places = pence """
    image = models.ImageField(upload_to='images')
    """ Allow images to be uploaded for our products """
    
    def __str__(self):
        return self.make  # A string will be returned with the make of rugby boot
        
        

    

