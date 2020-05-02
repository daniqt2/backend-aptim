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
    club = models.ForeignKey(
        'Club',
        related_name="members",
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
        on_delete= models.CASCADE
    )
    name = models.CharField(max_length=30)
    description =  models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.club, self.name)
        unique_slugify(self, slug_str)
        super(ClubGroup, self).save()
    
    def __str__(self):
        return self.name
    
class Channel(models.Model):
    club = models.ForeignKey(
        'Club',
        related_name="channels",
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
        slug_str = "%s %s" % (self.name, self.club)
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
        on_delete= models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text =  models.TextField(blank="false")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    votes = models.ManyToManyField(
         settings.AUTH_USER_MODEL,
         related_name="votes"
    )
    
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.thread, self.user)
        unique_slugify(self, slug_str)
        super(Comment, self).save()
    
class Event(models.Model):
    club = models.ForeignKey(
        'Club',
        related_name="events",
        on_delete= models.CASCADE
    )
    name = models.CharField(max_length=30)
    description =  models.CharField(max_length=400)
    date= models.DateTimeField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, **kwargs):
        slug_str = "%s %s" % (self.club, self.name)
        unique_slugify(self, slug_str)
        super(Event, self).save()
    
    