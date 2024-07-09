from django import template

register = template.Library()

@register.filter
def split_str(value, delimiter):
    return value.split(delimiter)

@register.filter
def make_range(value):
    return range(1, value + 1)

@register.filter
def get_question(obj, index):
    return getattr(obj, f"question_{index}", None)

@register.filter
def split_question(value):
    if value is None:
        return []
    return value.split('\\n')






