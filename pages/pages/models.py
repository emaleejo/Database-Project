from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class ContactDetail(models.Model):
    ContactID = models.IntegerField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    addr = models.ManyToManyField('Address')
    c_email = models.ManyToManyField('Email')

    def __str__(self):
        return '{0}'.format(self.user.username)


class Address(models.Model):
    cid = models.ForeignKey(ContactDetail, on_delete=models.CASCADE, default=1)
    addr = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return '{0}'.format(self.addr)


class Email(models.Model):
    cid = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)
    email = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return '{0}: {1}'.format(self.cid, self.email)


class Author(models.Model):
    AuthorID = models.IntegerField(primary_key=True,
                                   auto_created=True, unique=True)
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


class Supplier(models.Model):
    Name = models.CharField(max_length=45, primary_key=True)
    rep = models.OneToOneField('SupplierRep',
                               on_delete=models.CASCADE,
                               null=True)

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
        unique_together = (('first_name', 'last_name'),)

    def __str__(self):
        return '{0}, {1} {2}'.format(self.sid, self.first_name, self.last_name)


class Review(models.Model):
    title = models.CharField(max_length=50, null=True)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    belongs = models.ForeignKey('Book', on_delete=models.CASCADE, default=122)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages-browse')


class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=45)
    publish_date = models.DateField()
    price = models.FloatField()
    categorized = models.ManyToManyField('Category')
    author = models.ManyToManyField('Author')
    supplied = models.ForeignKey(Supplier, on_delete=models.CASCADE,
                                 default='Walmart')
    judgements = models.ManyToManyField(Review, null=True)

    def get_category(self):
        # Creates a string for the Category.
        # This is required to display genre in Admin.
        return ', '.join([c.__str__() for c in self.categorized.all()[:3]])

    def get_author(self):
        # Creates a string for the Author.
        # This is required to display genre in Admin.
        author_name = ', '.join(['{0} {1}'.format(a.first_name, a.last_name)
                                for a in self.author.all()[:3]])
        return author_name

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             blank=True, null=True)

    CustomerID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    ContactID = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.CustomerID)


class OrderItem(models.Model):
    ItemNumber = models.AutoField(primary_key=True)
    Item_Price = models.FloatField()
    # OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.OneToOneField(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0}'.format(self.item.title)


class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Order_Date = models.DateField(auto_now=True)
    Order_Value = models.FloatField(default=0)
    # cid = models.ForeignKey(User.id, on_delete=models.CASCADE, )
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return '{0}'.format(self.user.username)


class Phone(models.Model):
    ContactID = models.ForeignKey(ContactDetail, on_delete=models.CASCADE)
    number = models.CharField(max_length=13, primary_key=True)

    def __str__(self):
        return '{0}'.format(self.number)
