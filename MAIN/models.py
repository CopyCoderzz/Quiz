from django.db import models

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    exp=models.CharField(max_length=1000,null=True)
    clg_name=models.CharField(max_length=100,null=True)
    exam_name=models.CharField(max_length=100,null=True)
    exm_date=models.DateField(null=True)
    
    def __str__(self):
        return self.question


class Users(models.Model):
    # type=models.CharField(max_length=200)
    clg=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    username=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200)
    # login_id=models.IntegerField(null=True)

    def __str__(self):
        return self.username
    # def __str(self):
    #     return self.password


class college(models.Model):
    name=models.CharField(max_length=200,null=True)
    username=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.username


class login(models.Model):
    type=models.CharField(max_length=200)
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200)
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.username



class attend_exam(models.Model):
    s_email=models.CharField(max_length=200,null=True)
    exam_name=models.CharField(max_length=200)
    flag=models.CharField(max_length=200)



class Quizfile(models.Model):
    doc=models.FileField(upload_to="file")
    upload_date=models.DateField(null=True)
    exam_name=models.CharField(max_length=100,null=True)
    clg_name=models.CharField(max_length=100,null=True)
    exm_date=models.DateField(null=True)


class result(models.Model):
    s_name=models.CharField(max_length=100,null=True)
    college=models.CharField(max_length=100,null=True)
    exam=models.CharField(max_length=100,null=True)
    score=models.CharField(max_length=100,null=True)
    percentage=models.CharField(max_length=100,null=True)
    timetaken=models.CharField(max_length=100,null=True)
    correct=models.CharField(max_length=100,null=True)
    wrong=models.CharField(max_length=100,null=True)
    not_attempted=models.CharField(max_length=100,null=True)
    total=models.CharField(max_length=100,null=True)
    exm_date=models.DateField(null=True)




