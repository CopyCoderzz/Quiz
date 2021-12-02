from django.http.response import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, HttpResponse
from pyexpat.errors import messages
from django.contrib.auth.models import User, auth
from django.contrib import messages
import time
from .forms import *
from .models import *
import random
import itertools
from datetime import date
import docx
import smtplib

secret_key = "key"

print("quizzz")
# Create your views here.

def index(request):
    return render(request, "index11.html")



def loginPage(request):
    return render(request, 'login_index.html')


def signin(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            ob = login.objects.get(username=username, password=password)
            print(ob.type)
            # print(ob)
            if ob is not None:
                request.session['lg']='lin'
                if ob.type == "admin":
                    user_name = ob.name
                    request.session['name'] = user_name
                    request.session['lid'] = ob.username
                    request.session['lg']='true'
                    print("email id ",request.session['name'] )
                    print(user_name)
                    return render(request, "admin/admin_home.html", {'user10': user_name})
                else:
                    print("ytfajuysdfguayfg")
                    user_name = ob.name
                    request.session['name'] = user_name
                    request.session['lid'] = ob.username
                    request.session['lg']='true'
                    request.session['eg']='true'
                    print("email id fgdfg",request.session['lid'])
                    print(user_name)
                    return redirect('open_question')
                    # return render(request, "View_Quiz_List.html", {'data': user_name})
            else:
                return HttpResponse('<script>alert("Invalid cgfhfgchfgh");window.location="loginPage"</script>')
        else:
            return HttpResponse('<script>alert("Invalid User");window.location="loginPage"</script>')
    except Exception as e:
        messages.info(request,'Invalid Username or Password')
        return redirect('loginPage')

def open_question(request):
    if request.session['lg']=='true':
        user10=request.session['name']
        user = request.session['lid']
        clg1 = Users.objects.get(username=user)
        clg=clg1.clg
        obj = Quizfile.objects.filter(clg_name=clg)
        print("find college",clg)
        exm=attend_exam.objects.all().filter(s_email=request.session['lid'])
        exml=[]
        for ex in exm:
            exml.append(ex.exam_name)
        return render(request,'View_Quiz_List.html',{'data': obj,'user':user,'exml':exml,'user10':user10})
    else:
        return redirect('/loginPage')



def start(request,pk):
    if request.session['lg']=='true' and  request.session['eg']=='true':
        print("pk gfg",pk)
        obj = Quizfile.objects.get(exam_name=pk)
        exam=obj.exam_name
        print(exam)
        user10=request.session['name']

        #exams=attend_exam.objects.get(s_email=request.session['lid'])
        #for exam in exams: 
        #user1 = attend_exam.objects.create(s_email=request.session['lid'],flag=0)
        #user1.save()

        # attend_exam.objects.filter(s_email= request.session['lid']).update(exam_name=pk)
        # exam1=attend_exam.objects.get(s_email= request.session['lid'],exam_name=pk)
        # f=exam1.flag
        # print("exam name is",f)


        #if f==0:  
        return render(request,'start.html',{'obj':exam,'user10':user10})
    else:
        return redirect('/loginPage')
        #else:
        #    return HttpResponse('<script>alert("Already attended");window.location="/open_question"</script>')




# def get_type(value):
#     return type(value)

def home(request,pk):
        
        print("pk in home",pk)
        if request.method == 'POST':
            request.session['lg']='false'
            questions = QuesModel.objects.filter(exam_name=pk)
            score = 0
            wrong = 0
            correct = 0
            total = 0
            not_attempted = 0
            for q in questions:

                # for q in questions:
                total += 1
                print(" request pass")
                print(request.POST.get(q.question))
                
                print(q.ans)
                if request.POST.get(q.question) == q.ans:
                    score += 10
                    correct += 1
                    print("correct")
                elif request.POST.get(q.question) == None:
                    not_attempted += 1
                    print("not_attempted")
                else:
                    wrong += 1
                    print("wrong")
                print()
            percent1 = int(score / (total * 10) * 100)
            percent = ("%.2f" % percent1)
            bl=""
            if percent1>=75 :
                bl="Excellent"
            elif percent1 >= 50:
                bl="Very Good"
            elif  percent1 >= 25:
                bl="Good"
            else:
                bl="Failed! " 
            context = {
                'score': score,
                'timer': request.POST.get('timer'),
                'correct': correct,
                'wrong': wrong,
                'percent': percent,
                'total': total,
                'not_attempted': not_attempted,
                'pk':pk,
                'user10':request.session['name']
            }
            student = request.session['name']
            print("student name",student)
            u_id=request.session['lid'] 
            colg = Users.objects.get(username=u_id)
            clg=colg.clg
            print("colleg name checking",clg)
            tim=request.POST.get('timer')
            user1 = result.objects.create(score=score,timetaken=tim,correct=correct,wrong=wrong, percentage=percent,total=total,not_attempted=not_attempted,exam=pk,college=clg,s_name=student,exm_date=date.today())
            user1.save()
            a_and_e=""
            a=1
            for q in questions:
                a1=str(a)
                a_and_e+=a1
                a_and_e+=".)"
                a_and_e+=q.question
                a_and_e+='\n'
                a_and_e+='\n'
                a_and_e+="Answer:"
                a_and_e+=q.ans
                a_and_e+='\n'
                a_and_e+='\n'
                a_and_e+=q.exp
                a_and_e+='\n'
                a_and_e+='\n'
                a_and_e+='-----------------------------------------------------------------------'
                a_and_e+='\n'
                a+=1
            ae=a_and_e.encode('ascii', 'replace').decode('ascii')
            gmail_user = 'newtoneinstein2921@gmail.com'
            gmail_password = '4103230848'
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login(gmail_user,gmail_password)
                print("Login Success")
                subject = 'Your Results'
                body = f'''Hi, {student}
                Your Test Quiz Result
                ----------------------------------
                Score : {score}
                Time taken : {tim} Seconds
                Correct : {correct}
                Wrong : {wrong}
                Percentage : {percent}%
                Total Questions : {total}
                Not Attempted : {not_attempted}
                {bl}
                --------------------------------------
                Answer And Explanation
                --------------------------------------
                {ae}
                '''

                msg = f'Subject:{subject}\n\n{body}'

                smtp.sendmail(gmail_user,u_id,msg)
            return render(request, 'result.html', context)
            
            
        else:
            
            if request.session['lg']=='true' and request.session['eg']=='true':
                
                request.session['eg']='false'
                questions = QuesModel.objects.filter(exam_name=pk)
                
                # question number random
                print("styfdu")
                s = questions.count()
                print(s)
                d = []
                e = []
                for i in range(s):
                    e.append(int(i + 1))
                    d.append(int(i + 1))
                random.shuffle(d)
                
                # random.shuffle(p)
                # print(p)
                # Question Random
                ob1 = QuesModel.objects.values_list('question', flat=True)
                print(ob1)
                a1 = []
                for i in ob1:
                    a1.append(str(i))
                print(a1)
                #Shuffled Questions
                ss=[]
                for i in d:
                    
                    ss.append(a1[i-1])


                # OPTION1 Random
                ob2 = QuesModel.objects.values_list('op1', flat=True)
                print(ob2)
                a2 = []
                for i in ob2:
                    a2.append(str(i))
                print(a2)
                # OPTION2 Random
                ob3 = QuesModel.objects.values_list('op2', flat=True)
                print(ob3)
                a3 = []
                for i in ob3:
                    a3.append(str(i))
                print(a3)
                # OPTION3 Random
                ob4 = QuesModel.objects.values_list('op3', flat=True)
                print(ob4)
                a4 = []
                for i in ob4:
                    a4.append(str(i))
                print(a4)
                # OPTION4 Random
                ob5 = QuesModel.objects.values_list('op4', flat=True)
                print(ob5)
                a5 = []
                for i in ob5:
                    a5.append(str(i))
                print(a5)
                # OPTION5 Random
                ob6 = QuesModel.objects.values_list('ans', flat=True)
                print(ob6)
                a6 = []
                for i in ob6:
                    a6.append(str(i))
                print(a6)
                # OPTION6 Random
                ob7 = QuesModel.objects.values_list('exp', flat=True)
                print(ob7)
                a7 = []
                for i in ob7:
                    a7.append(str(i))

                print(a7)
                '''context = {
                    'questions':questions
                }'''
                print("list")
                print(type(d[0]))
                #print(a1[0])
                mylist = zip(e, d, ss)
                # b2 = zip(a2, a1)
                # b3 = zip(a3, a1)
                # b4 = zip(a4, a1)
                # b5 = zip(a5, a1)
                # context = {
                #     'mylist': mylist,
                # }
                
                context = {
                    'mylist': mylist,
                    'e': e,
                    'd': d,
                    'a1': a1,
                    # 'b2': b2,
                    # 'b3': b3,
                    # 'b4': b4,
                    # 'b5': b5,
                    'a6': a6,
                    'a7': a7,
                    # 'a1':a1,
                    'a2':a2,
                    'a3':a3,
                    'a4':a4,
                    'a5':a5,
                    'ss':ss,
                    'user10':request.session['name']

                }
            
                user1 = attend_exam.objects.create(s_email=request.session['lid'],exam_name=pk)
                user1.save()
                return render(request, 'Home.html', context)
            else:
                return redirect('/loginPage')



def register(request):
    print("register")
    ob = college.objects.values_list('name', flat=True)
    print(ob)
    a = []
    for i in ob:
        a.append(str(i))
    print(a)
    # Entry.objects.values_list('column_name', flat=True)
    return render(request, 'signup_index.html', {'datas': a})

def signup(request):
        if request.method == 'POST':
            # type=request.POST['type']
            clg = request.POST['clg']
            name = request.POST['Name']
            email = request.POST['Email']
            phone = request.POST['Phone']
            password = request.POST['Password']
            cpassword = request.POST['Cpassword']
            if password == cpassword:
                if Users.objects.filter(username=email).exists():
                    messages.info(request, "Username already exists")
                    return HttpResponse('<script>alert("Username Exists");window.location="register"</script>')
                else:
                    type = "user"
                    user1 = login.objects.create(type=type, username=email, password=password, name=name)
                    user = Users.objects.create(clg=clg, name=name, username=email, phone=phone, password=password)
                    
                    user.save()
                    user1.save()
                    print(user)
                    return redirect('loginPage')
            else:
                print("Password doesnot match")
                return HttpResponse('<script>alert("Password doesnot match");window.location="register"</script>')
        else:
            return render(request, 'signup_index.html')


def college_reg(request):
    return render(request, 'admin/admin_signup.html')


def college_signup(request):
        if request.method == 'POST':
            name = request.POST['Name']
            email = request.POST['Email']
            phone = request.POST['Phone']
            password = request.POST['Password']
            cpassword = request.POST['Cpassword']
            if password == cpassword:
                if Users.objects.filter(username=email).exists():
                    messages.info(request, "Username already exists")
                    return HttpResponse('<script>alert("Username Exists");window.location="college_reg"</script>')
                else:
                    type = "admin"
                    user1 = login.objects.create(type=type, username=email, password=password, name=name)
                    user = college.objects.create(name=name, username=email, phone=phone, password=password)
                    
                    user.save()
                    user1.save()
                    print(user)
                    return redirect('loginPage')
            else:
                print("Password doesnot match")
                return HttpResponse('<script>alert("Password doesnot match");window.location="college_reg"</script>')
        else:
            return render(request, 'admin_signup.html')


def addQuestion(request):
    if request.session['lg']=='true':
        if request.user.is_staff:
            form = addQuestionform()
            if (request.method == 'POST'):
                form = addQuestionform(request.POST)
                if (form.is_valid()):
                    form.save()
                    return redirect('/')
            context = {'form': form}
            return render(request, 'addQuestion.html', context)
        else:
            return redirect('home')


def showanswer(request,pk):
    if request.session['lg']=='true':
        context = {'users': QuesModel.objects.filter(exam_name=pk)}
        return render(request, 'QuesAnswers.html', context)
    else:
        return redirect('/loginPage')



def view_user(request):
    if request.session['lg']=='true':
        user10=request.session['name']
        print(request.session['name'])
        clg = request.session['name']
        obj = Users.objects.filter(clg=clg)
        return render(request, 'admin/view_user.html', {'data': obj,'user10':user10})
    else:
        return redirect('/loginPage')



def upload_file1(request):
    if request.session['lg']=='true':
        user10=request.session['name']
        return render(request, 'admin/upload_file.html',{'user10':user10})
    else:
        return redirect('/loginPage')


def ReadingTextDocuments(doc):
        doc = docx.Document(doc)
        completedText = []
        for paragraph in doc.paragraphs:
            completedText.append(paragraph.text)
        return '\n'.join(completedText)

#@login_required
def upload_file(request):
    if request.session['lg']=='true':
        if request.method == "POST":
            exm_name = request.POST['exam_name']
            # ob=Quizfile.objects.get(exam_name=exm_name)
            # print(ob)
            if Quizfile.objects.filter(exam_name=exm_name).exists():
                messages.info(request, "Username already exists")
                return HttpResponse('<script>alert("Exam Name Exists");window.location="upload_file1"</script>')
            else:
                doc = request.FILES.get('file1')
                # doct=request.POST.get('file1')
                # print(doct)
                exam = request.POST['exam_name']
                exm_date = request.POST['exam_date']
                clg = request.session['name']
                print("College Name",clg)
                user = Quizfile.objects.create(doc=doc, upload_date=date.today(), exam_name=exam, clg_name=clg, exm_date= exm_date)
                user.save()
                # file2.save()
                print("file uploaded")
                op_a = []
                op_b = []
                op_c = []
                op_d = []
                exp = []
                que = []
                ans = []
                ques = []
                quiz_text = ReadingTextDocuments(doc)
                quiz_list2 = quiz_text.splitlines()
                quiz_list = []
                for string in quiz_list2:
                    if string != "":
                        quiz_list.append(string)
                print(quiz_list)
                a = 0
                y=0
                question=""
                for i in quiz_list:
                    a = 0
                    if i.startswith('a)'):
                        a = 1
                        op_a.append(i)
                        # quiz_list.remove(i)
                    if i.startswith('b)'):
                        a = 1
                        op_b.append(i)
                        # quiz_list.remove(i)
                    if i.startswith('c)'):
                        a = 1
                        op_c.append(i)
                        # quiz_list.remove(i)
                    if i.startswith('d)'):
                        a = 1
                        op_d.append(i)
                        # quiz_list.remove(i)
                    if i.startswith('Explanation'):
                        a = 1
                        exp.append(i)
                        # quiz_list.remove(i)
                    if a == 0:
                        que.append(i)
                for i in que:
                    if i.startswith('Ans:'):
                        ans.append(i)

                        y = 1
                    else:
                        question+=i
                    if y == 1:
                        ques.append(question)
                        question = ""
                        y = 0
                db=len(op_a)
                for i in range(db):
                    if ans[i].endswith('a'):
                        ans1 = op_a[i]
                    elif ans[i].endswith('b'):
                        ans1 = op_b[i]
                    elif ans[i].endswith('c'):
                        ans1 = op_c[i]
                    else :
                        ans1 = op_d[i]

                    user1 = QuesModel.objects.create(question=ques[i], op1=op_a[i], op2=op_b[i], op3=op_c[i], op4=op_d[i], ans=ans1, exp=exp[i], exm_date=exm_date,exam_name=exam, clg_name=clg)
                    user1.save()
                print(len(op_a))
                print(len(op_b))
                print(len(op_c))
                print(len(op_d))
                print(len(exp))

                print(ans)
                print(ques)
                #print(que)
                #return redirect('upload_file1')
                return HttpResponse('<script>alert("Added Successfully");window.location="upload_file1"</script>')
        else:
            return render(request, 'admin/upload_file.html')
    else:
        return redirect('/loginPage')


def logoutPage(request):
    auth.logout(request)
    request.session.clear
    request.session['lg']="false"
    return redirect('/')
