from django.shortcuts import render
from app.models import QUESTION
import requests
import csv
import os
# Create your views here.
sheetly_header={
    "Authorization":"Bearer 66"
    }
sheetly_endpoint="https://api.sheety.co/78eda28988cc9dbe69ca0a6bb25df255/core/tests"

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
        
            # "name":name,
            "q1":q1,
            "q2":q2,
            "q3":q3,
            "q4":q4,
            "q6":q6,
            "q7":q7,
            "q8":q8,
            "q9":q9,
            # "content":content,
            # "tech":tech,
            # "design":design,
            # "cultural":cultural,
            # "creativity":creativity,
            # "hospitality":hospitality,
            # "logistics":logistics,  
        }

        response = requests.post(url=sheetly_endpoint, json=sheetly_params, headers=sheetly_header)
#         if response.status_code == 200:
# #     # Successful API call
#          print("Data posted successfully.")
#         else:

# #     # Error in API call
#           print("Status code:", response.status_code)
#           print("Response content:", response.content)
#           print("Error while posting data to Sheety.")
# ./home/ubuntu/project/CORE_FORM23/participants.csv
        with open('participants.csv', 'a', newline='') as csvfile:                 
                    spamwriter= csv.writer(csvfile)
                    data1=[name,q1,q2,q3,q4,q6,q7,q8,q9,content,tech,design,cultural,creativity,hospitality,logistics]
                    spamwriter.writerow(data1)

        return render(request,'thankyou.html')
    return render(request,'thankyou.html')