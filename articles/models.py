from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() #문자열 빈 값 저장은 null이 아니라 ''
    # blank :데이터 유효성과 관련되어 있다. 아무런 값이 넘어오지 않아도 저장할 수 있다. 
    # null : DB와 관련되어 있다.
    # '', Null
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    # on_delete에 models.CASCADE는 article 삭제시 comment 함께 삭제
    # article.comment_set => article.comments 변경해주는게 related_name
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Mete:
        ordering = ['-pk']
    def __str__(self):
        return self.content
    