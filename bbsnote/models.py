from django.db import models

# Create your models here.

#게시글모델
class Board(models.Model): 
    subject = models.CharField(max_length=200) 
    content = models.TextField()
    create_date = models.DateTimeField() 
    #객체 호출했을 때 리턴해주는 값
    def __str__(self):
        return self.subject
    
#댓글모델
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE) 
    content = models.TextField()
    create_date = models.DateTimeField()