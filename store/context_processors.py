from .models import Category
from .models import ProductType


def categories(request):
    return {"categories": Category.objects.filter(level=0)}

def product_type(request):
    return{"product_type": ProductType.objects.filter(level=0)}