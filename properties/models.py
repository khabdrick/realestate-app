from django.db import models

# bathroom, bedroom, squarefeet, location, property type, Property description
PROPERTY_TYPE_CHOICES= (
    ('type1', 'Rent'),
    ('type2', 'Sell'),
   
)


class Property(models.Model):

    property_name = models.CharField(max_length=225)
    property_description = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    no_of_bedrooms = models.IntergerField(max_length=15, decimal_places=0)
    no_of_bathrooms = models.IntergerField(max_length=15, decimal_places=0)
    squarefeet = models.IntergerField(max_length=15, decimal_places=2)
    amount = models.IntergerField(max_length=15, decimal_places=0)
    property_type = models.CharField(max_length=120, choices=PROPERTY_TYPE_CHOICES)
