from django.shortcuts import render

def show_skills(request):
    return render(request,'skills.html')
