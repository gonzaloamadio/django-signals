from django.apps import AppConfig


class UserProfile2Config(AppConfig):
    name = 'user_profile_2'
    verbose_name = 'profiles2'

    def ready(self):
        # This one does not give error, but does not work
        #import signals  # noqa

        import user_profile_2.signals  # noqa

