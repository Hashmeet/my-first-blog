from django.db import models
from django.utils import timezone
class Post(models.Model):
	
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.CharField(max_length=50, null=True,blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Choice(models.Model):
    title=models.ForeignKey(Post)
    votes=models.IntegerField(default='0')

class SignUp(models.Model):
    name=models.CharField(max_length=100,null=False)
    email_id=models.EmailField()


