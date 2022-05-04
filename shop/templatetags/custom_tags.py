import math

from django import template
from shop.models import *

register = template.Library()


@register.filter(name='get_first_price')
def get_first_price(id):
    price = Variants.objects.filter(product_id=id).first().price
    return price


@register.filter(name='get_first_sale_price')
def get_first_sale_price(id):
    sale_price = Variants.objects.filter(product_id=id).first().sale_price
    return sale_price


@register.filter(name='get_first_sale_percent')
def get_first_sale_price(id):
    sale_percent = Variants.objects.filter(product_id=id).first().sale_percent()
    return sale_percent


@register.filter(name='get_first_color')
def get_first_color(id):
    color = Variants.objects.filter(product_id=id).first().color
    return color


@register.filter(name='get_variants')
def get_variants(id):
    variants = Variants.objects.filter(product_id=id).order_by('?')
    return variants


@register.filter(name="get_first_word")
def get_first_word(string):
    first_word = string.split(" ")[0]
    return first_word


@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url


@register.filter(name="get_overall_rate")
def get_overall_rate(slug):
    prods = ProductReview.objects.filter(product__slug=slug)
    self_rate = 0
    if prods:
        for rev in prods:
            self_rate += int(rev.rate)
        return round(self_rate / prods.count(), 1)
    else:
        return self_rate


@register.filter(name="count_five")
def count_five(slug):
    prods = ProductReview.objects.filter(product__slug=slug)
    return prods.filter(rate=5).count()


@register.filter(name="count_four")
def count_five(slug):
    prods = ProductReview.objects.filter(product__slug=slug)
    return prods.filter(rate=4).count()


@register.filter(name="count_three")
def count_five(slug):
    prods = ProductReview.objects.filter(product__slug=slug)
    return prods.filter(rate=3).count()


@register.filter(name="count_two")
def count_five(slug):
    prods = ProductReview.objects.filter(product__slug=slug)
    return prods.filter(rate=2).count()


@register.filter(name="count_one")
def count_five(slug):
    prods = ProductReview.objects.filter(product__slug=slug)
    return prods.filter(rate=1).count()


@register.filter(name="get_list")
def get_list(rate):
    list = []
    for i in range(0, int(rate)):
        list.append(i)
    return list
