from django import template

register = template.Library()
@register.filter
def in_category(things, category):
    return things.filter(state=category)