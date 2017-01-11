from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    last_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    middle_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    birthday = models.DateField()
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=50,null=False, blank=False,)
    MALE = 'М'
    FEMALE = 'Ж'
    gender_choices = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )
    sex = models.CharField(choices=gender_choices, max_length=1, default=MALE)

class Computer(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(null=True, blank=True, upload_to="images/",
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    description = models.TextField(max_length=2000, null=False, blank=False)
    price = models.IntegerField()

class Order(models.Model):
    user = models.ForeignKey('User')
    computer = models.ForeignKey('Computer')
    address = models.CharField(max_length=255,null=False, blank=False)
    delivery_date = models.DateTimeField()
    count = models.ForeignKey('Computer', related_name="Count")
