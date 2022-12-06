from django.shortcuts import render
from django.db import connection

# Create your views here.


def login(request):
    return render(request, 'login.html')


def question(request):
    if request.method == 'POST':
        question = request.POST["question"]

    with connection.cursor() as cursor_1:
        cursor_1.execute("select * from question")
        row1 = cursor_1.fetchall()
    return render(request, 'question.html', {"row1": row1})


def course(request):
    with connection.cursor() as cursor_1:
        cursor_1.execute("select * from question")
        row1 = cursor_1.fetchall()
    return render(request, 'course.html', {"row1": row1})
