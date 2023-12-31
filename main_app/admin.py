from django import forms
from django.contrib import admin
from django.utils.html import format_html
from main_app.models import Section, Category, Product
from modeltranslation.admin import TranslationAdmin


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"
        widgets = {
            "image": forms.FileInput(attrs={"required": False}),
        }


class DisplayImageMixin:
    def display_image(self, obj) -> str:
        if obj.image:
            return format_html('<img src="{}" width="50"/>'.format(obj.image.url))
        else:
            return "No Image"

    display_image.short_description = "Image"


class SectionAdmin(DisplayImageMixin, TranslationAdmin):
    form = SectionForm
    list_display = ("id", "name", "display_image")


admin.site.register(Section, SectionAdmin)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "image": forms.FileInput(attrs={"required": False}),
        }


class ProductAdmin(DisplayImageMixin, TranslationAdmin):
    form = ProductForm
    list_display = ("id", "name", "display_image")


admin.site.register(Product, ProductAdmin)
