import os

from django.db import models


def get_file_name(model_name, filename):
    _, extension = os.path.splitext(filename)
    return "_".join(model_name.split()).lower() + extension


def image_path_section(model_instance, filename):
    filename = get_file_name(model_instance.name, filename)
    return os.path.join("uploads/sections/", filename)


def image_path_product(model_instance, filename):
    filename = get_file_name(model_instance.name, filename)
    return os.path.join("uploads/products/", filename)


class Section(models.Model):
    name = models.CharField(max_length=40, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to=image_path_section)


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    section_id = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to=image_path_product)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
