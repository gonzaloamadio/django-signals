from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from django.conf import settings

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    logger.info('[user_profile_2 receiver]')
    if created:
        logger.info('[user_profile_2 receiver if]')
        Profile2.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    logger.info('[user_profile_2 receiver save]')
    instance.profile2.save()
