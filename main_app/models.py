from django.db import models

# Create your models here.

class Apps(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    title = models.CharField(max_length=100)
    description = models.TextField()
    URL_website = models.URLField(null=True, blank=True)
    URL_download = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='apps/' , null=True, blank=True)

    show = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True , null=True , blank=True)


    def __str__(self):
        return self.full_name


class BlueTick_info(models.Model):
    about_me = models.TextField()
    phone = models.CharField(max_length=13)
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)

    image = models.ImageField(upload_to='banner/' , null=True, blank=True)

    def __str__(self):
        return self.about_me[:11]


class ads_banner(models.Model):
    image = models.ImageField(upload_to='adsBanner/' )

