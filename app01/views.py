from django.shortcuts import render,HttpResponse
def happy(request):
    return HttpResponse("欢迎来到天上人间,bug修复完毕，请大家继续嗨")

# Create your views here.
