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
    

class Events(models.Model):
    id = models.AutoField(primary_key= True)
    main_title = models.CharField(max_length=200)
    secondary_title = models.CharField(max_length=200)
    date = models.DateTimeField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image1 = models.FileField(upload_to = 'images')
    image2 = models.FileField(upload_to = 'images')
    image3 = models.FileField(upload_to = 'images')
    image4 = models.FileField(upload_to = 'images')
    image5 = models.FileField(upload_to = 'images')
    image6 = models.FileField(upload_to = 'images')
    venue = models.ForeignKey(Location ,on_delete = models.CASCADE)
    winners = models.ManyToManyField(Winner, blank= True)
    rules = models.ForeignKey(Rules,on_delete = models.CASCADE)
    prizes = models.ForeignKey(Prize, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.main_title} - {self.date} - {self.venue}'
    

