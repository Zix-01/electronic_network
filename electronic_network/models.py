from django.db import models


class NetworkNode(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.ForeignKey('Contacts', on_delete=models.CASCADE, verbose_name='contacts')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='product')
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='suppliers')
    outstanding_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Network Node"
        verbose_name_plural = "Network Nodes"


class Factory(NetworkNode):
    level = models.PositiveIntegerField(default=0)


class RetailNetwork(NetworkNode):
    level = models.PositiveIntegerField(default=1)


class Entrepreneur(NetworkNode):
    level = models.PositiveIntegerField(default=2)


class Contacts(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    node = models.ForeignKey(NetworkNode, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} - {self.model}"
