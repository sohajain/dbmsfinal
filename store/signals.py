from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart,BookOrder
from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@receiver(post_save,sender=Cart)
def adjust_stock(sender,instance,**kwargs)