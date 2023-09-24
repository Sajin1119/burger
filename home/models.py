from django.db import models




class BookTable(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)  # You can adjust the max length as needed
    email = models.EmailField(max_length=254)
    persons = models.CharField(max_length=2)
    date=models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.name

class Testimonial(models.Model):
    name=models.CharField(max_length=50)
    img = models.ImageField(upload_to='test', blank=True, null=True)
    product=models.CharField(max_length=50,default="crab")
    desc=models.CharField(max_length=300)
    def __str__(self) :
        return self.name


class Offer(models.Model):
    title=models.CharField(max_length=20)
    img=models.ImageField(upload_to='offer')
    des=models.TextField(null=True)
    offPercentage=models.CharField(max_length=2)
    def __str__(self) :
        return self.title
    
class Menu(models.Model):
    img=models.ImageField(upload_to='menu')
    title=models.CharField(max_length=50)
    desc=models.TextField(null=True)
    mrp=models.CharField(max_length=5)
    def __str__(self) -> str:
        return self.title