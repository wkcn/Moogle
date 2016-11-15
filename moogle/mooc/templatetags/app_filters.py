from django import template

register = template.Library()

@register.filter(name='dec2hex')
def dec2hex(value):
    return hex(int(value))