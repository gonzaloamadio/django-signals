from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    logger.info('[user_profile receiver]')
    if created:
        logger.info('[user_profile receiver if]')
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    logger.info('[user_profile receiver save]')
    instance.profile.save()
