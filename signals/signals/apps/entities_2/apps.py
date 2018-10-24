from django.apps import AppConfig
#from django.conf import settings
#from django.db.models.signals import post_save


class Entities2Config(AppConfig):
    name ='entities_2'

    def ready(self):
        import entities_2.signals
#        from .signals import user_create_profile
#        from django.apps.authentication import User
#        post_save.connect(user_create_profile, sender=User)
