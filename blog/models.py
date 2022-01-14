from django.db import models
from django.utils import timezone
# User and Post model will have a relation ship (1 to many relationship)
# User can post n times while the post can only have 1 user
from django.contrib.auth.models import User 

""" Things we will save in the database:
        Users, Posts,"""

class Post(models.Model):
        title = models.CharField(max_length=50)
        content = models.TextField() # Basically allows unrestricted texts
        # It will not change the date it was posted whenever u update it (auto_now=True) as well
        # as not restrict you for changing the date (auto_now_add=True)
        date_posted = models.DateTimeField(default=timezone.now)
        author = models.ForeignKey(User, on_delete=models.CASCADE) # models.CASCADE will delete the post when user is deleted

        def __str__(self):
                return self.title
