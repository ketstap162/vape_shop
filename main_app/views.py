from django.shortcuts import render
from main_app.models import Section, Product


def home_page_view(request):
    context = {
        "sections": Section.objects.prefetch_related("category_set"),
        "products": Product.objects.select_related("category_id__section_id")
    }

    if request.GET.get("section"):
        query_filter = request.GET.get("section").replace("_", " ")
        context["products"] = context["products"].filter(category_id__section_id__name=query_filter)

    if request.GET.get("category"):
        query_filter = request.GET.get("category").replace("_", " ")
        context["products"] = context["products"].filter(category_id__name=query_filter)

    return render(request, "base.html", context=context)
