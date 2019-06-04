from django.db import models

# Create your models here.


class Teacher(models.Model):
    tid=models.AutoField(primary_key=True)
    tname=models.CharField(max_length=32)
    classes=models.ManyToManyField("Klass")
    def __str__(self):
         return self.tname

class Grade(models.Model):
    gid=models.AutoField(primary_key=True)
    gname=models.CharField(max_length=32)

    def __str__(self):
         return self.gname

class Klass(models.Model):
    kid=models.AutoField(primary_key=True)
    kname=models.CharField(max_length=32)
    grade=models.ForeignKey("Grade",on_delete=models.CASCADE)
    def __str__(self):
         return self.kname


class Student(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=32)
    gender=models.IntegerField(choices=((0,"男"),(1,"女")))
    cls=models.ForeignKey("Klass",on_delete=models.CASCADE)
    def __str__(self):
         return self.sname


class Course(models.Model):
     cid=models.AutoField(primary_key=True)
     cname=models.CharField(max_length=32)
     teacher=models.ForeignKey("Teacher",on_delete=models.CASCADE)
     def __str__(self):
         return self.cname


class Score(models.Model):
    sid=models.AutoField(primary_key=True)
    student=models.ForeignKey("Student",on_delete=models.CASCADE)
    course=models.ForeignKey("Course",on_delete=models.CASCADE)
    score=models.IntegerField()

    def __str__(self):
        return str(self.student)+str(self.course)+str(self.score)

    # class Meta:
    #     unique_together = (("student","course"),)

