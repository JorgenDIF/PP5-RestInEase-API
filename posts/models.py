from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]

    mood_choices = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('excited', 'Excited'),
        ('relaxed', 'Relaxed'),
        ('stressed', 'Stressed'),
        ('adventurous', 'Adventurous'),
        ('grateful', 'Grateful'),
        ('lonely', 'Lonely'),
        ('angry', 'Angry'),
        ('in_love', 'In Love')
    ]

    category_choices = [
        ('nature', 'Nature'),
        ('cafe', 'Cafe'),
        ('home', 'Home'),
        ('workplace', 'Workplace'),
        ('park', 'Park'),
        ('beach', 'Beach'),
        ('mountain', 'Mountain'),
        ('city', 'City'),
        ('countryside', 'Countryside'),
        ('water', 'Water')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )
    mood = models.CharField(
        max_length=32, choices=mood_choices, default='happy'
    )
    category = models.CharField(
        max_length=32, choices=category_choices, default='nature'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
