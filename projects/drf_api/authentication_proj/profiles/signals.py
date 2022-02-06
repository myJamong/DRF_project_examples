from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    User로 부터 post_save signal을 받아서 receiver가 처리한다. --> Trigger 역할을 하는 것
    - User 인스턴스가 생성되면 Profile도 생성되도록 한다.
    """
    if created:
        Profile.objects.create(user=instance)