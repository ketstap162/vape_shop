from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=40, unique=True)
    image = models.ImageField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    section_id = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
