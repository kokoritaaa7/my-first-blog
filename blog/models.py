from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):

    # models.ForeignKey : 다른 모델에 대한 링크
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.CharField : 글자 수가 제한된 텍스트를 정의 (짧은 문자열)
    title = models.CharField(max_length=200)
    # models.TextField : 글자 수가 제한없는 긴 텍스트를 위한 속성
    text = models.TextField()
    # models.DateTimeField : 날짜와 시간
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title