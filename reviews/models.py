from django.db import models
from django.urls import reverse
# Create your models here.
class Review(models.Model):
    email = models.
    product = models.ForeignKey(, on_delete=models.CASCADE, )
    comment = models.TextField(null=False)

    created_review = models.DateTimeField(auto_now_add=True)
    updated_review = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created_review', 'updated_review']

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.name])



