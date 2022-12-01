from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='catagory'
        verbose_name_plural='catagories'
    def get_url(self):
        return reverse('prod_cat', args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.CharField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product_img')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField(default=False)
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)