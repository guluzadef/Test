from django.db import models
from base_user.models import MyUser

User=MyUser





# Create your models here.
class Site_name(models.Model):
    icon=models.ImageField(upload_to="site_icon")
    name=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Menu(models.Model):
    name=models.CharField(max_length=255)
    url=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Main(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=400)
    icon_food=models.ImageField(upload_to="main_icon")
    food_count=models.PositiveIntegerField()
    video_url=models.CharField(max_length=255)


    def __str__(self):
        return f"{self.title}"



class First(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Second(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Meals(models.Model):
    name=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(choices=(('Morning',("Morning")),
                                        ('Lunch',("Lunch")),
                                        ('Supper',("Supper")),
                                        ),default=2,max_length=244)
    gram_one_porsion=models.PositiveIntegerField()
    ingredients=models.CharField(max_length=500)
    aditional_info=models.TextField()
    delivery_type=models.CharField(choices=(('Shef',("Shef")),
                                        ('User',("User")),
                                        ),default=1,max_length=244)

    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name},{self.author}"



class Footer(models.Model):
    description=models.CharField(max_length=300)
    number=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    instagram=models.CharField(max_length=255)
    instagram_img=models.ImageField(upload_to="media_insta")

    def __str__(self):
        return f"{self.description}"


