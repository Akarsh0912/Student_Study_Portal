from django.db import models
from django.contrib.auth.models import User


#This class will create a database model or table for NOTES Module
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name="Notes"
        verbose_name_plural="Notes"

      
#This class will create a database model or table for HOMEWORK Module
class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description=models.TextField()
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)


    def __str__(self):
        return self.subject 

    class Meta:
        verbose_name="Homework"
        verbose_name_plural="Homework"



##This class will create a database model or table for TO-DO Module
class ToDo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name="ToDo"
        verbose_name_plural="ToDo"


        
