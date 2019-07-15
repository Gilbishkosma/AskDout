from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.conf import settings
from ask.models import Profile
from django.contrib.auth.signals import user_logged_in, user_logged_out

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,email=instance.email)
        
