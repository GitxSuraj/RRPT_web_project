from django.db import models


# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    real_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    image = models.ImageField(upload_to="main_page/images", default="")
    image2 = models.ImageField(upload_to="main_page/images", default="")
    image3 = models.ImageField(upload_to="main_page/images", default="")
    image4 = models.ImageField(upload_to="main_page/images", default="")
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class TShirts(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    real_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    image = models.ImageField(upload_to="main_page/images", default="")
    image2 = models.ImageField(upload_to="main_page/images", default="")
    image3 = models.ImageField(upload_to="main_page/images", default="")
    image4 = models.ImageField(upload_to="main_page/images", default="")
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class Trousers(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    real_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    image = models.ImageField(upload_to="main_page/images", default="")
    image2 = models.ImageField(upload_to="main_page/images", default="")
    image3 = models.ImageField(upload_to="main_page/images", default="")
    image4 = models.ImageField(upload_to="main_page/images", default="")
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    desc_type = models.CharField(max_length=25, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.user_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:20] + "..."


class JobApplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    work = models.CharField(max_length=150, default="")
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=111)

    def __str__(self):
        return self.name