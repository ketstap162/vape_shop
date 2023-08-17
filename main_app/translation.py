from modeltranslation.translator import register, TranslationOptions
from main_app.models import Section, Category, Product


@register(Section)
class SectionTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("description",)
