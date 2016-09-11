from django import template
register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})


@register.filter(name='fieldtype')
def field_type(field):
        return field.field.widget.__class__.__name__
