from django.shortcuts import render
from main_app.models import Section, Category, Product


def home_page_view(request):
    context = {
        "sections": Section.objects.prefetch_related("category_set"),
        "products": Product.objects.select_related("category_id")
    }
    print(vars(context["sections"][0]))
    return render(request, "base.html", context=context)
