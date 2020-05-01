from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.models import Channel

def add_slug(self):
        slug = slugify[self.name]
        random_str = gen_random_str()
        return slug + "-" + random_str
        