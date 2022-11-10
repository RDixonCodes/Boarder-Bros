from tkinter import CASCADE
from django.db import models
import re

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        register_with_email = User.objects.filter(email = postData['email'])
        if len(register_with_email) >= 1:
            errors['duplicate'] = "Email already exists."
        if len(postData['password']) < 5:
            errors['password'] = "Password must be at least 5 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password must match!"
        if len(postData['user_name']) < 3:
            errors['user_name'] = "User name must be at least 3 characters"
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        # if len(postData['user_image']):
        #     errors['user_image'] = "User must have a photo"
        return errors

class ItemManager(models.Manager):
    def item_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "Title must contain at least 3 characters"
        if len(postData['catagory']) == " ":
            errors['catagory'] = "Item must have a catagory"
        if len(postData['item_photo_url']) == " ":
            errors['item_photo_url'] = "Item must have a photo"
        if len(postData['desc']) ==  " ":
            errors['desc'] = "Item must contain a description"
        return errors

class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_image = models.ImageField(upload_to=None, height_field=None, width_field=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<User object: user_name: {self.user_name}, name: {self.last_name, self.first_name}, email: {self.email}>"

class Item(models.Model):
    title = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50)
    item_photo_url = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    user_item = models.ForeignKey(User, related_name="user_items", on_delete=models.CASCADE)
    # added_item = models.ManyToManyField(User, related_name='added_items')
    traded_item = models.ManyToManyField(User, related_name="traded_items")
    sold_item = models.ManyToManyField(User, related_name="sold_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()

    def __repr__(self):
        return f"<Item object: title: {self.title}, catagory: {self.catagory}, price: {self.price}, desc: {self.desc}>"

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
