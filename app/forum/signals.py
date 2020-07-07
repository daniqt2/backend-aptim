from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

def add_slug(self):
        slug = slugify[self.name]
        random_str = gen_random_str()
        return slug + "-" + random_str

# @receiver(post_save, sender=Request)
# def make_author(sender, instance, created, **kwargs):
#     if created:
#         MembershipRequest.objects.create(name=instance.author)