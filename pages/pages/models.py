from django.db import models

# Create your models here.


class ContactDetail(models.Model):
    ContactID = models.IntegerField(auto_created=True, primary_key=True)
    
    def __str__(self):
        return '{0}'.format(self.ContactID)
class Address(models.Model):
    cid = models.ForeignKey(ContactDetail, on_delete=models.CASCADE, primary_key=True)
    addr = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return '{0}, {1}'.format(self.cid, self.addr)
class Email(models.Model):
    cid = models.ForeignKey(ContactDetail,on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=45, primary_key=True)


class Author(models.Model):
    AuthorID = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    Date_of_Birth = models.DateField()
    ContactID = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)

    def __str__(self):
        return'{0}, {1}'.format(self.last_name, self.first_name)
    
class Category(models.Model):
    CategoryCode = models.IntegerField(primary_key=True, unique=True)
    CategoryDescription = models.CharField(max_length=45)

    def __str__(self):
        return self.CategoryDescription

class Book(models.Model):
    isbn = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=45)
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=3,decimal_places=2)
    categorized = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    
class Customers(models.Model):
    CustomerID = models.IntegerField(primary_key=True,unique=True, auto_created=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    ContactID = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.CustomerID)


class Order(models.Model):
    OrderID = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    Order_Date = models.DateField()
    Order_Value = models.IntegerField()
    cid = models.ForeignKey(Customers, on_delete=models.CASCADE, )

    def __str__(self):
        return '{0}'.format(self.OrderID)

class OrderItems(models.Model):
    ItemNumber = models.IntegerField(primary_key=True)
    Item_Price = models.IntegerField()
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.ItemNumber)

class Phone(models.Model):
    ContactID = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)
    number = models.CharField(max_length=13, primary_key=True)

    def __str__(self):
        return '{0}'.format(self.number)
