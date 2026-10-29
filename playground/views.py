from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, F, Count, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product, Customer
from tags.models import TaggedItem


# Create your views here.

def calculate(x, y):
    return x + y


def say_hello(request):
    # query_set = Product.objects.all()
    products = Product.objects.filter(unit_price__range=(200, 300), inventory__gt=20)
    # products = Product.objects.filter(Q(inventory__gt=20) | ~Q(unit_price__lt=20))
    # products = Product.objects.filter(inventory=F('collection__id'))
    # products = Product.objects.order_by('title')
    # products = Product.objects.order_by('-title')[0]
    # products = Product.objects.earliest('title')
    # products = Product.objects.values('title', 'unit_price','collection__title').distinct()
    # products = Product.objects.only('title','unit_price')
    # products = Product.objects.defer('title','unit_price')
    # products = Product.objects.select_related('collection').all()
    # products = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # products = Product.objects.prefetch_related('orderitem_set').select_related('collection').all()
    # products = Product.objects.aggregate(count = Count('id'))
    # products = Product.objects.aggregate(count = Count('id'))
    # products = Product.objects.annotate(x=Value(True))
    # products = Customer.objects.annotate(full_name=Concat(F('first_name'), F('last_name')))

    ###############lookups
    # 1. برابری دقیق
    # products = Product.objects.filter(title__exact='Laptop')
    #
    # # 2. برابری بدون حساسیت به حروف بزرگ و کوچک
    # products = Product.objects.filter(title__iexact='laptop')
    #
    # # 3. وجود عبارت در عنوان
    # products = Product.objects.filter(title__contains='phone')
    #
    # # 4. جست‌وجوی عنوان بدون حساسیت به حروف
    # products = Product.objects.filter(title__icontains='phone')
    #
    # # 5. عنوان‌هایی که با عبارت مشخصی شروع می‌شوند
    # products = Product.objects.filter(title__startswith='Sam')
    #
    # # 6. عنوان‌هایی که با عبارت مشخصی تمام می‌شوند
    # products = Product.objects.filter(title__endswith='Pro')
    #
    # # 7. قیمت بزرگ‌تر از 200
    # products = Product.objects.filter(unit_price__gt=200)
    #
    # # 8. قیمت بزرگ‌تر یا مساوی 200
    # products = Product.objects.filter(unit_price__gte=200)
    #
    # # 9. قیمت کوچک‌تر از 300
    # products = Product.objects.filter(unit_price__lt=300)
    #
    # # 10. قیمت کوچک‌تر یا مساوی 300
    # products = Product.objects.filter(unit_price__lte=300)
    #
    # # 11. قیمت بین 200 و 300، با احتساب دو سر بازه
    # products = Product.objects.filter(unit_price__range=(200, 300))
    #
    # # 12. موجودی یکی از مقادیر مشخص‌شده باشد
    # products = Product.objects.filter(inventory__in=[10, 20, 30])
    #
    # # 13. محصولاتی که collection ندارند
    # products = Product.objects.filter(collection__isnull=True)
    #
    # # 14. محصولاتی که collection دارند
    # products = Product.objects.filter(collection__isnull=False)

    # discounted_price = ExpressionWrapper(F('unit_price')*0.8,output_field=DecimalField())
    # products = Product.objects.annotate(price=discounted_price)

    # content_type = ContentType.objects.get_for_model(Product)
    # x = TaggedItem.objects.select_related('tag').filter(content_type=content_type, object_id=1)

    # cach-senario 1
    # queryset = Product.objects.all()
    # list(queryset)
    # queryset[0]

    # cach - senario 2
    # queryset = Product.objects.all()
    # queryset[0]
    # list(queryset)

    # products = Product.objects.all()
    #
    # for product in products:
    #     print(product.title)
    #     print(product.collection.title)
    #
    #     for promotion in product.promotions.all():
    #         print(promotion.description)
    res = calculate(10, 20)
    return render(request, 'hello.html', {'name': 'Aida', 'products': products})
