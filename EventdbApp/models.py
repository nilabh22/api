from distutils.command import upload
from django.db import models

# Create your models here.

class Prize(models.Model):
    prizes = models.CharField(max_length=999)

    def __str__(self):
        return f'Prizes: {self.prizes}'


class Winner(models.Model):
    position = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=500)
    prizes = models.ForeignKey(Prize, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.college} (Position: {self.position})'


class Location(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=300)
    

    def __str__(self):
        return f'{self.name}'

class Rules(models.Model):
    primary_title = models.CharField(max_length=200)
    rules = models.TextField()

    def __str__(self):
        return self.primary_title
    

class Speaker(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=50)
    organization = models.CharField(max_length=199)
    education = models.CharField(max_length=299)
    description = models.CharField(max_length=999)

    def __str__(self):
        return f'{self.name} - {self.organization}'

class Image(models.Model):
    main_title =models.CharField(max_length=200, blank =True, null=True)
    image1 = models.FileField(upload_to = 'images',blank = True, null=True)
    image2 = models.FileField(upload_to = 'images',blank = True, null=True)
    image3 = models.FileField(upload_to = 'images',blank = True, null=True)
    image4 = models.FileField(upload_to = 'images',blank = True, null=True)
    image5 = models.FileField(upload_to = 'images',blank = True, null=True)
    image6 = models.FileField(upload_to = 'images',blank = True, null=True)
    
    def __str__(self):
        return self.main_title
    

class Events(models.Model):
    id = models.AutoField(primary_key= True)
    main_title = models.CharField(max_length=200, blank=True, null= True)
    secondary_title = models.CharField(max_length=200, blank=True, null = True)
    date = models.DateTimeField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    eventEnded = models.CharField(max_length=5, default="False")
    eventRegistrationLink = models.CharField(max_length = 99, blank=True, null=True)
    eventGallery = models.ForeignKey(Image,on_delete=models.CASCADE,blank=True, null=True)
    venue = models.ForeignKey(Location ,on_delete = models.CASCADE, blank= True, null =True)
    winners = models.ManyToManyField(Winner, blank= True)
    rules = models.ForeignKey(Rules,on_delete = models.CASCADE)
    prizes = models.ForeignKey(Prize, on_delete=models.CASCADE, null = True, blank=True)
    speaker =models.ForeignKey(Speaker, on_delete=models.CASCADE, null =True, blank = True)

    def __str__(self):
        return f'{self.main_title} - {self.date} - {self.venue}'
    

