from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    publ_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def update_post(self, title=None, content=None) -> None:
        if title:
            self.title = title

        if content:
            self.content = content

        self.save()

    def delete_post(self) -> None:
        self.delete()
