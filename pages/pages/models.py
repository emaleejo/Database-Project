from django.db import models

# Create your models here.


class ContactDetail(models.Model):
    ContactID = models.IntegerField(auto_created=True, primary_key=True)
    
    def __str__(self):
        return '{0}'.format(self.ContactID)

class Address(models.Model):
    cid = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)
    addr = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return '{0}, {1}'.format(self.cid, self.addr)

class Email(models.Model):
    cid = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)
    email = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return '{0}: {1}'.format(self.cid, self.email)


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
    CategoryDescription = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.CategoryDescription

class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=45)
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=3,decimal_places=2)
    categorized = models.ManyToManyField('Category')
    author = models.ManyToManyField('Author')
    # list_author = ', '.join(['{0} {1}'.format(a.first_name, a.last_name) for a in author.all()[:3]])
    
    def get_category(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([c.__str__() for c in self.categorized.all()[:3]])

    def get_author(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(['{0} {1}'.format(a.first_name, a.last_name) for a in self.author.all()[:3]])

    def __str__(self):
        return self.title

    
class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    # CustomerID = models.IntegerField(primary_key=True,unique=True, auto_created=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    ContactID = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.CustomerID)


class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    # OrderID = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    Order_Date = models.DateField()
    Order_Value = models.IntegerField()
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE, )

    def __str__(self):
        return '{0}'.format(self.OrderID)

class OrderItem(models.Model):
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

class Supplier(models.Model):
    Name = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return self.Name

class SupplierRep(models.Model):
    sid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    cell_number = models.CharField(max_length=13)
    work_number = models.CharField(max_length=13)
    email = models.CharField(max_length=45)

    class Meta:
        unique_together = (('first_name','last_name' ),)

    def __str__(self):
        return '{0}, {1} {2}'.format(self.sid, self.first_name, self.last_name)