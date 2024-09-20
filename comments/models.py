from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Comment model, related to User and Post

    This model has been customized to include a 'feeling' field,
    allowing users to select an emotion that represents their comment.
    
    In the future, the 'feeling' field will be refactored into a separate
    model to provide more flexibility and scalability, enabling easier
    management of the feeling options and dynamic updates without
    requiring changes to the code.
    """
    FEELING_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('excited', 'Excited'),
        ('bored', 'Bored'),
        ('confused', 'Confused')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    feeling = models.CharField(max_length=10, choices=FEELING_CHOICES,
                               blank=True)  # New field

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
