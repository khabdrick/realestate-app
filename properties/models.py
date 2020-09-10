import random
import os
from django.conf import settings
# from django.core.files.storage import FileSystemStorage

from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse


from realestateapp.utils import unique_slug_generator, get_filename
from agency.models import Agency

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "Properties/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

class PropertiesQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True, not_available=False)

    def featured(self):
        return self.filter(featured=True, active=True, not_available=False)

    def search(self, query):
        lookups = (Q(location__icontains=query) | 
                  Q(property_type__icontains=query) |
                  Q(bathrooms__icontains=query) |
                  Q(bedrooms__icontains=query) |
                  Q(price__icontains=query) |
                  Q(__icontains=query)
                  )
        return self.filter(lookups).distinct()

class PropertiesManager(models.Manager):
    def get_queryset(self):
        return PropertiesQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Properties.objects.featured() 
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Properties.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


PROPERTY_CHOICE = (
		('Bungalow', 'Bungalow'),
	    ('Condo', 'Condo'),
	    ('Duplex', 'Duplex'),
	    ('Flat', 'Flat'),
	    ('Self Contain', 'Self Contain'),
	    ('Storey Building', 'Storey Building'),
	    ('2 Storey Building', '2 Storey Building'),
	)


ROOMS_CHOICES = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
	)


ACTIVATION_CHOICES = (
		('For Sale','For_Sale'),
		('For Rent','For_Rent')
	)

# class Agency(models.Model):
#     agent               = models.CharField(max_length=120)

#     def __str__(self):
#         return self.agent



class Properties(models.Model):
    agent                   = models.ForeignKey(Agency,blank=True, null=True, on_delete=models.CASCADE)
    slug                    = models.SlugField(blank=True,unique=True)
    title                   = models.CharField(max_length=120)
    description             = models.TextField(null=True, blank=True)
    location                = models.CharField(max_length=150)
    property_type           = models.CharField(max_length=120, choices=PROPERTY_CHOICE,default="flat")
    property_size           = models.IntegerField(default=0)
    price                   = models.CharField(max_length=18)
    bedrooms                = models.IntegerField(default=1, choices=ROOMS_CHOICES)
    bathrooms               = models.IntegerField(default=1, choices=ROOMS_CHOICES)
    image1                  = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image2                  = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image3                  = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image4                  = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image5                  = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image6                  = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        		= models.BooleanField(default=False)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True)
    availability 			= models.CharField(max_length=120, default='For_Sale',choices=ACTIVATION_CHOICES)
    not_available 			= models.BooleanField(null=True, blank=True, default=False)
 
    objects = PropertiesManager()

    def get_absolute_url(self):
        #return "/Properties/{slug}/".format(slug=self.slug)
        return reverse("Properties:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @property
    def name(self):
        return self.title


def Properties_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(Properties_pre_save_receiver, sender=Properties) 


