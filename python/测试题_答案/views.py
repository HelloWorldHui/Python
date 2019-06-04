from django.shortcuts import render,HttpResponse

# Create your views here.
from app01.models import *


def query(request):

    '''
            import random
            for i in range(200):
                try:
                    Score.objects.create(student_id=random.randint(1,31),course_id=random.randint(1,5),score=random.randint(30,100))
                except:
                    pass


           import random
            for i in range(200):
                try:
                    student_id=random.randint(1, 31)
                    course_id=random.randint(1, 5)
                    if not Score.objects.filter(student_id=student_id,course_id=course_id):
                        Score.objects.create(student_id=student_id, course_id=course_id,
                                             score=random.randint(30, 100))
                except:
                    print(i)



            2、查询学生总人数；
            3、查询“生物”课程和“物理”课程成绩都及格的学生id和姓名；
            4、查询每个年级的班级数，取出班级数最多的前三个年级；
            5、查询平均成绩最高的学生的id和姓名以及平均成绩；
            6、查询每个年级的学生人数；
            7、查询每位学生的学号，姓名,平均成绩；
            8、查询学生编号为“2”的学生的姓名、该学生成绩最高的课程名及分数；
            9、查询姓“李”的老师的个数和所带班级数；
            10、查询班级数小于5的年级id和年级名；
            11、查询教过课程超过2门的老师的id和姓名；
            12、查询学过编号“1”课程和编号“2”课程的同学的学号、姓名；
            13、查询所带班级数最多的老师id和姓名；
            14、查询有课程成绩小于60分的同学的学号、姓名；
            15、查询男生、女生的人数，按倒序排列；
            16、 查询各个课程及相应的选修人数；
            17、 查询同时选修了物理课和生物课的学生id和姓名；
            18、 检索“3”课程分数小于60，按分数降序排列的同学学号；
            19、 查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
            20、 查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
    '''

    from django.db.models import Count,Max,Min,Avg,F

    # # 1 查询学生总人数；
    # ret1=Student.objects.count()
    # print(ret1)
    # # 2 查询生物课程或物理课程成绩都及格的学生id和姓名；
    # ret2=Score.objects.filter(course__cname__in=["生物","物理"],score__gte=60).values("student__sname","student__pk")
    # ret2=Score.objects.filter(course__cname__in=["生物","物理"],score__gte=60).values("student__pk").annotate(c=Count("course")).filter(c=2)

    # 3 查询每个年级的班级数，取出班级数最多的前三个年级名称；
    # ret=Grade.objects.annotate(c=Count("klass")).order_by("-c")[0:3]
    # print(ret)

    #
    # # 4 查询平均成绩最高的学生的id和姓名以及平均成绩；

    # ret=Score.objects.values("student").annotate(avg_score=Avg("score")).order_by("-avg_score").values("student__sname","student__pk","avg_score")[0]
    # print(ret)


    # # 5 查询每个年级的学生人数；
    # ret=Grade.objects.annotate(c=Count("klass__student__pk")).values("gname","c")
    # print(ret)


    # # 6 查询每位学生的学号，姓名,平均成绩；
    ret=Student.objects.values("sid","sname").annotate(avg_score=Avg("score__score"))
    print(ret)
    #ret=Student.objects.annotate(avg_score=Avg("score__score")).values("sid","sname","avg_score")


    # ret=Student.objects.annotate(avg_score=Avg("score__score")).values("sname","pk","avg_score")
    # print(ret)

    # 7 查询学生编号为“2”的学生的姓名、该学生成绩最高的课程名及分数；
    ret=Student.objects.filter(pk=2).order_by("-score__score").values("sname","score__course__cname","score__score")[0]
    print(ret)
    ret=Score.objects.filter(student__pk=2).order_by("-score").values("student__sname","course__cname","score")[0]
    print(ret)

    # ret=Score.objects.values("student").annotate(max_score=Max("score")).values("student__sname","max_score","course__cname")
    # ret = Score.objects.filter(student=2).order_by("-score").values("score", "course__cname", "student__sname")[0]
    # print(ret)

    # 8 查询每一个姓“李”的老师所带班级数；
    ret=Teacher.objects.filter(tname__istartswith="小").annotate(c=Count("classes")).values("tname","c")
    print(ret)

    # ret=Teacher.objects.filter(tname__startswith="李").annotate(c=Count("classes")).values("tname","c")

    # # 9 查询班级数小于5的年级id和年级名；
    Grade.objects.annotate(c=Count("klass")).filter(c__lt=5).values("pk","gname")

    # ret=Grade.objects.annotate(c=Count("klass")).filter(c__lt=5).values("pk","gname")

    # #10 查询教过课程超过2门的老师的id和姓名；

    ret=Teacher.objects.annotate(c=Count("course")).filter(c__gt=2).values("pk","tname")


    # ret=Teacher.objects.annotate(c=Count("course")).filter(c__gt=2).values("pk","tname")


    # # 11 查询学过编号“1”课程和编号“2”课程的同学的学号、姓名；

    ret=Student.objects.filter(score__course__cid=1).filter(score__course__cid=2).values("pk","sname")
    print(ret)

    # ret=Student.objects.filter(score__course__cid__in=[1,2]).values("pk","sname")
    #

    # # 12 查询所带班级数最多的老师id和姓名；
    ret=Teacher.objects.annotate(c=Count("classes")).order_by("-c").values("pk","tname")[0]
    # ret=Teacher.objects.annotate(c=Count("classes")).order_by("-c").values("pk","tname")[0]

    # # 13 查询有课程成绩小于60分的同学的学号、姓名；

    ret=Score.objects.filter(score__lt=60).values("student__sname","student__pk").distinct()
    print(ret)
    # ret=Score.objects.filter(score__lt=60).values("student__sname","student__pk").distinct()
    #



    # # 14 查询男生、女生的人数，按倒序排列；
    ret=Student.objects.values("gender").annotate(c=Count(1)).order_by("-c")
    # ret=Student.objects.values("gender").annotate(c=Count(1)).order_by("c").values("gender","c")

    # # 15 查询各个课程及相应的选修人数；
    ret=Score.objects.values("course").annotate(c=Count(1)).values("course__cname","c")
    print(ret)
    # ret=Score.objects.values("course").annotate(c=Count("student")).values("course__cname","c")

    # # 16 查询同时选修了物理课和生物课的学生id和姓名；
    # ret=Student.objects.filter(score__course__cname__in=["物理","生物"]).values("pk","sname")


    # # 17 检索“3”课程分数小于60，按分数降序排列的同学学号；

    Score.objects.filter(course_id=3,score__lt=60).order_by("-score").values("student_id")
    # ret=Score.objects.filter(course__cid=3,score__lt=60).order_by("score").values("student__sname","student__pk")
    #
    # # 18 查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；

    ret=Score.objects.values("course_id").annotate(c=Avg("score")).order_by("c","-course_id")
    # ret=Score.objects.values("course").annotate(avg_score=Avg("score")).order_by("avg_score","course")
    #
    # # 19 查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
    ret=Course.objects.annotate(max_score=Max("score__score"),min_score=Min("score__score")).values("pk","max_score","min_score")
    # ret=Course.objects.annotate(max_score=Max("score__score"),min_score=Min("score__score")).values("cname","max_score","min_score")


    return HttpResponse("查询成功!")