from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class 바로 아래에 있는 것들은 속성들이고 
# def 행위라고 할 수 있다.
# Post 타입의 변수를 객체라고 할 수있다. post 에 대한 특정 문자열 변수가 필요하면
# __str__을 쓰게 된다.