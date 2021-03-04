from django.db import models
from pytils.translit import slugify ##Helps to fill in slug field even when channel name is in russian


class Influencer(models.Model):
    channel_name = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True, blank=True)
    date_created = models.DateField("When created", auto_now_add=True)
    date_updated = models.DateField("When updated", auto_now=True)

    def __str__(self):
        return self.channel_name

    # class Meta()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.channel_name)
        super().save(*args, **kwargs)


class Content(models.Model):
    channel_name = models.ForeignKey('Influencer', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_of_publication = models.DateField()
    video_name = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.date_of_publication} - {self.channel_name} - {self.video_name}'


class DailyStats(models.Model):
    video_url = models.ForeignKey('Content', on_delete=models.CASCADE, related_name='content')
    date_of_update = models.DateField(auto_now=True)
    video_views = models.IntegerField()
    video_comments = models.IntegerField()
    video_likes = models.IntegerField()
    video_dislikes = models.IntegerField()

    def __str__(self):
        return f'{self.date_of_update} - {self.video_url.channel_name} - {self.video_url.video_name} - {self.video_views}'

    class Meta:
        ordering = ['-video_url__date_of_publication', '-video_views']