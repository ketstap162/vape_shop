import os

from django.db import models


def get_file_name(model_name, filename):
    _, extension = os.path.splitext(filename)
    return "_".join(model_name.split()).lower() + extension


def image_path_section(model_instance, filename):
    filename = get_file_name(model_instance.name, filename)
    return os.path.join("sections/", filename)


def image_path_product(model_instance, filename):
    filename = get_file_name(model_instance.name, filename)
    return os.path.join("products/", filename)


class Section(models.Model):
    name = models.CharField(max_length=40, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to=image_path_section)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    section_id = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def name_without_spaces(self):
        return self.name.replace(" ", "_")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to=image_path_product)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField()

    def get_description(self):
        if len(self.description) >= 50:
            return self.description[:47].strip() + "..."
        else:
            return self.description

    def __str__(self):
        return self.name
