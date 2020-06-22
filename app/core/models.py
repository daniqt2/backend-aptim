from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# from core.utils ge
from django.db.models.signals import pre_save, post_save
from .utils import unique_slugify
# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        """creates normal user"""
        if not email:
            raise ValueError('Must enter email')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password):
        """creates superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    identif = models.CharField(max_length=16, default = 'none')
    is_active = models.BooleanField(default=True)
    is_apmaster = models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number = models.CharField(max_length=9, null=True,
        blank= True)
    club = models.ForeignKey(
        'Club',
        related_name="members",
        on_delete= models.CASCADE,
        null=True,
        blank= True
    )
    group = models.ForeignKey(
        'ClubGroup',
        related_name="gmembers",
        on_delete= models.CASCADE,
        null=True,
        blank= True
    )
    event = models.ForeignKey(
        'Event',
        related_name="attendees",
        on_delete= models.CASCADE,
        null=True,
        blank= True
    )
    objects = UserManager()
    USERNAME_FIELD = 'email'
    
class Club(models.Model):
    name = models.CharField(max_length=30)
    description =  models.TextField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.name, 'aptim')
        unique_slugify(self, slug_str)
        super(Club, self).save()
    
    def __str__(self):
        return self.name

class ClubGroup(models.Model):
    club = models.ForeignKey(
        'Club',
        related_name="groups",
        null=True,
        blank= True,
        on_delete= models.CASCADE
    )
    name = models.CharField(max_length=30)
    description =  models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.name, self.description)
        unique_slugify(self, slug_str)
        super(ClubGroup, self).save()
    
    def __str__(self):
        return self.name
    
class Channel(models.Model):
    club = models.ForeignKey(
        'Club',
        related_name="channels",
        null=True,
        blank= True,
        on_delete= models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="author",
        on_delete=models.SET_NULL,
        null=True, 
    )
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=30)
    description =  models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
        
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.name, self.author)
        unique_slugify(self, slug_str)
        super(Channel, self).save()
        
    def __str__(self):
        return self.name
    
class Topic(models.Model):
    channel = models.ForeignKey(
        'Channel',
        related_name="topics",
        on_delete= models.CASCADE
    )
    name = models.CharField(max_length=30)
    description =  models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.channel, self.name)
        unique_slugify(self, slug_str)
        super(Topic, self).save()
    
    def __str__(self):
        return self.name
    
class Thread(models.Model):
    topic = models.ForeignKey(
        'Topic',
        related_name="threads",
        on_delete= models.CASCADE
    )
    name = models.CharField(max_length=30)
    text =  models.TextField(blank="false")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="creator",
        on_delete=models.SET_NULL,
        default=None,
        null=True, 
    )
    likes =models.IntegerField(null=True,
        blank=True)
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.topic, self.name)
        unique_slugify(self, slug_str)
        super(Thread, self).save()
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    thread = models.ForeignKey(
        'Thread',
        related_name="comments",
        null=True,
        on_delete= models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comment_author",
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True
    )
    text =  models.TextField(blank="false")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    votes = models.IntegerField(null=True,
        blank=True)
    
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.thread, self.user)
        unique_slugify(self, slug_str)
        super(Comment, self).save()
    
class Event(models.Model):
    EVENT_TYPES = (
    ("C", "Competition"),
    ("T", "Training"),
    ("E", "Event"),
    )
    club = models.ForeignKey(
        'Club',
        related_name="events",
        null=True,
        blank= True,
        on_delete= models.CASCADE
    )
    title = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    description =  models.CharField(max_length=400)
    date= models.DateTimeField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_type = models.CharField(max_length=9,
                  choices=EVENT_TYPES,
                  default="C")
    
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.title, self.description)
        unique_slugify(self, slug_str)
        super(Event, self).save()
    
    def __str__(self):
        return self.name
    
    