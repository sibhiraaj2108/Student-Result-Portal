from django.db import models

class Result(models.Model):
    student_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.subject}"