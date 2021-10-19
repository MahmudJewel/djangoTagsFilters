from django import template
register = template.Library()

@register.filter(name='addd')
def addd(a,b):
    return a+b

@register.filter(name='sub')
def sub(a,b):
    return a-b

@register.filter(name='mul')
def mul(a,b):
    return a*b

@register.filter(name='divide')
def divide(a,b):
    return a/b

@register.filter(name='reminder')
def reminder(a,b):
    return a%b
