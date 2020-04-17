from django.contrib.auth.models import User
from django.db.models.signals import post_save  # used to send a signal every time a user is created
from django.dispatch import receiver  # this now receives the signal as it is a decorator.
from userprofile.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("Created", created)
    if created:
        Profile.objects.create(user=instance)
