from django.shortcuts import render
from app.models import QUESTION
import requests
import csv
# Create your views here.
sheetly_header={
    "Authorization":"Bearer 123456"
    }
sheetly_endpoint="https://api.sheety.co/f1d94ed59a4ac790c11c1e068d55788c/hellooo/sheet1"

def core(request):
    if request.method=='POST':
        name=request.POST['name']
        q1=request.POST['q1']
        q2=request.POST['q2']
        q3=request.POST['q3']
        q4=request.POST['q4']        
        q6=request.POST['q6']
        q7=request.POST['q7']
        q8=request.POST['q8']
        q9=request.POST['q9']
        content=int(request.POST['content'])
        tech=int(request.POST['tech'])
        design=int(request.POST['design'])
        cultural=int(request.POST['cultural'])
        creativity=int(request.POST['creativity'])
        hospitality=int(request.POST['hospitality'])
        logistics=int(request.POST['logistics'])
        data=QUESTION.objects.create(
        name=name,
        q1=q1,
        q2=q2,
        q3=q3,
        q4=q4,       
        q6=q6,
        q7=q7,
        q8=q8,
        q9=q9,
        content=int(content),
        tech=int(tech),
        design=int(design),
        cultural=int(cultural),
        creativity=int(creativity),
        hospitality=int(hospitality),
        logistics=int(logistics),
        )
        data.save()

        sheetly_params = {
        "workout": {
            "name":name,
            "q1":q1,
            "q2":q2,
            "q3":q3,
            "q4":q4,
            "q6":q6,
            "q7":q7,
            "q8":q8,
            "q9":q9,
            "content":content,
            "tech":tech,
            "design":design,
            "cultural":cultural,
            "creativity":creativity,
            "hospitality":hospitality,
            "logistics":logistics,  
        }
        }
        response = requests.post(url=sheetly_endpoint, json=sheetly_params, headers=sheetly_header)
        with open('participants.csv', 'a', newline='') as csvfile:                 
                    spamwriter= csv.writer(csvfile)
                    data1=[q1,q2,q3,q4,q6,q7,q8]
                    spamwriter.writerow(data1)

        return render(request,'thankyou.html')
    return render(request,'core.html')

