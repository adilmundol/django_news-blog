from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class News(models.Model):
    image = models.ImageField(upload_to='product', default='path/to/default/image.jpg')  # Provide a valid default image path
    heading = models.CharField(max_length=30)
    details = models.TextField()
    name = models.CharField(max_length=30)
    para = models.TextField()
    date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.heading

