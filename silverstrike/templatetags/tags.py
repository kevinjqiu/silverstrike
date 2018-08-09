import locale
from django import template


register = template.Library()


@register.filter
def negate(value):
    return -value


@register.filter
def currency(value):
    return locale.currency(value, grouping=True)