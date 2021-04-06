from django import template

register = template.Library()


@register.filter(name='multiplicar')
def multiplicar(a, b):
    return a * b


@register.filter(name='somar')
def somar(a, b):
    return a + b
