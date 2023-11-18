from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    publ_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def update_post(self, title=None, content=None):
        if title:
            self.title = title

        if content:
            self.content = content

        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_posts_published_before(cls, date: timezone):
        return cls.objects.filter(publ_time__lt=date)

    @classmethod
    def get_posts_published_after(cls, date: timezone):
        return cls.objects.filter(publ_time__gte=date)