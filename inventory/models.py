from django.db import models
# from django.contrib.auth.models import User
from django_mysql.models import ListCharField
from colorfield.fields import ColorField
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
# Create your models here.

# Crew Neck Men Model

SIZE_CHOICES = (('M', 'M'), ('L', 'L'), ('XL', 'XL'),('XXL', 'XXL'))

THEMES = (("Anime","Anime"),("Drip and Doodle","Drip and Doodle"),("Abstract","Abstract"),("Music and Bands","Music and Bands"),("Movies and Series","Movies and Series"),("Typography","Typography"),("Sports","Sports"),("Marvel and DC","Marvel and DC"),("Sanskriti","Sanskriti"),("Persona","Persona"))

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# class colorF(models.Model):


# Images all

class crewNeckImg(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name

class DropCutImg(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name

class OversizedImg(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name
class crewNeckMen(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc=models.CharField(max_length=500)
    # color= ColorField(verbose_name='Color')
    size = MultiSelectField(choices=SIZE_CHOICES, max_choices=4,max_length=15)
    quantity = models.IntegerField(null=True,blank=True)
    M_R_P = models.DecimalField(max_digits=50, decimal_places=2)
    offer_price = models.DecimalField(max_digits=50, decimal_places=2)
    discount_price = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ]
    )
    prod_id = models.CharField(max_length=50,unique=True, blank=True, null=True,validators=[alphanumeric])
    images = models.ManyToManyField(crewNeckImg)

    def __str__(self):
        return self.prod_name

class DropCutMen(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc=models.CharField(max_length=500)
    # color= ColorField(verbose_name='Color')
    size = MultiSelectField(choices=SIZE_CHOICES, max_choices=4,max_length=15)
    quantity = models.IntegerField(null=True,blank=True)
    M_R_P = models.DecimalField(max_digits=50, decimal_places=2)
    offer_price = models.DecimalField(max_digits=50, decimal_places=2)
    discount_price = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ]
    )
    prod_id = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    images = models.ManyToManyField(DropCutImg)

    def __str__(self):
        return self.prod_name

class OversizedMen(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc=models.CharField(max_length=500)
    # color= ColorField(verbose_name='Color')
    size = MultiSelectField(choices=SIZE_CHOICES, max_choices=4,max_length=15)
    quantity = models.IntegerField(null=True,blank=True)
    M_R_P = models.DecimalField(max_digits=50, decimal_places=2)
    offer_price = models.DecimalField(max_digits=50, decimal_places=2)
    discount_price = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ]
    )
    prod_id = models.CharField(max_length=50,unique=True, blank=True, null=True, validators=[alphanumeric])
    images = models.ManyToManyField(OversizedImg)

    def __str__(self):
        return self.prod_name

class men(models.Model):
    crew_neck = models.ManyToManyField(crewNeckMen,blank=True,null=True)
    drop_cut=models.ManyToManyField(DropCutMen,blank=True,null=True)
    oversized = models.ManyToManyField(OversizedMen,blank=True,null=True)

# Women

class crewNeckWomen(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc=models.CharField(max_length=500)
    # color= ColorField(verbose_name='Color')
    size = MultiSelectField(choices=SIZE_CHOICES, max_choices=4,max_length=15)
    quantity = models.IntegerField(null=True,blank=True)
    M_R_P = models.DecimalField(max_digits=50, decimal_places=2)
    offer_price = models.DecimalField(max_digits=50, decimal_places=2)
    discount_price = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ]
    )
    prod_id = models.CharField(max_length=50,unique=True, blank=True, null=True,validators=[alphanumeric])
    images = models.ManyToManyField(crewNeckImg)

    def __str__(self):
        return self.prod_name

class DropCutWomen(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc=models.CharField(max_length=500)
    # color= ColorField(verbose_name='Color')
    size = MultiSelectField(choices=SIZE_CHOICES, max_choices=4,max_length=15)
    quantity = models.IntegerField(null=True,blank=True)
    M_R_P = models.DecimalField(max_digits=50, decimal_places=2)
    offer_price = models.DecimalField(max_digits=50, decimal_places=2)
    discount_price = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ]
    )
    prod_id = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    images = models.ManyToManyField(DropCutImg)

    def __str__(self):
        return self.prod_name

class OversizedWomen(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc=models.CharField(max_length=500)
    # color= ColorField(verbose_name='Color')
    size = MultiSelectField(choices=SIZE_CHOICES, max_choices=4,max_length=15)
    quantity = models.IntegerField(null=True,blank=True)
    M_R_P = models.DecimalField(max_digits=50, decimal_places=2)
    offer_price = models.DecimalField(max_digits=50, decimal_places=2)
    discount_price = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ]
    )
    prod_id = models.CharField(max_length=50,unique=True, blank=True, null=True, validators=[alphanumeric])
    images = models.ManyToManyField(OversizedImg)

    def __str__(self):
        return self.prod_name

class women(models.Model):
    crew_neck = models.ManyToManyField(crewNeckWomen,blank=True,null=True)
    drop_cut=models.ManyToManyField(DropCutWomen,blank=True,null=True)
    oversized = models.ManyToManyField(OversizedWomen,blank=True,null=True)

# Main Form
class main(models.Model):
    Color_name = models.CharField(max_length=100)
    Color_code = ColorField(verbose_name='Color')
    Themes =MultiSelectField(choices=THEMES, max_choices=10,max_length=500) 
    Men = models.ManyToManyField(men,blank=True,null=True)
    women=models.ManyToManyField(women,blank=True,null=True)