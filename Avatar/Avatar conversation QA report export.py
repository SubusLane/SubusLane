#from pandasgui import show
import pandas as pd
import requests
import os
import time
import zipfile


def get_duplicates(row):
    working = qa_report[qa_report["ac_id"] == row.ac_id]
    working = working[working["session"] != row.session]
    objects_list = working["object"].unique()
    if row.object in objects_list:
        return row.object
    else:
        return "n"


job_id_appen='1905705' #Add job id
targetdir_appen=r'C:\Users\subha\Appen\Falcon Messenger Avatars Testing 2021 - Documents\General\Data Collection\01 Tracker\Conversations\Source' #Add folder location

def get_QAreport(job_id,targetdir):
    job_id = job_id
    targetdir = targetdir
    #job_id = job_id
    #cmd = 'curl -X POST "https://api.appen.com/v1/jobs/' + job_id+"/regenerate\" -d \"type=full\" -d \"key=u_pFAGCs-drX9ST13y2p\""
    
    headers = {'Authorization': 'Token token=pvgbMxCLGsS72ZwsnuYj'}
    data = {'type': 'full'}
    response = requests.post('https://api.appen.com/v1/jobs/'+job_id+'/regenerate', headers=headers, data=data)    
    print(response) #Just for debug
    #os.system(response)
    time.sleep(20)
    #cmd = 'curl -L -X GET "https://api.appen.com/v1/jobs/' + job_id+".csv"+ '" -d "type=full" -d "key=u_pFAGCs-drX9ST13y2p" -o "' + job_id +".zip\""
    data = {'type': 'full'}
    response = requests.get('https://api.appen.com/v1/jobs/'+job_id+'.csv', headers=headers, data=data)   
    print(response) #Just for debug
    #os.system(response)
    targetdir = targetdir
    #with zipfile.ZipFile(job_id +".zip","r") as zip_ref:
    #    zip_ref.extractall(targetdir)
    with open(targetdir+"\\"+job_id+".zip", 'wb') as f:   #Saving the zip locally
        f.write(response.content)
    with zipfile.ZipFile(targetdir+"\\"+job_id +".zip","r") as zip_ref: #Extraction in folder
        zip_ref.extractall(targetdir)
    time.sleep(10)
    #os.remove(targetdir+"\\"+job_id+".zip")


get_QAreport(job_id_appen,targetdir_appen)  #Calling function

qa_report = pd.read_csv(targetdir_appen+"\\f"+job_id_appen+".csv")

columns = ['ac_id',
           '_worker_id',
           '_created_at',
           '_started_at',
           'session_name',
           'video01_s3',
           'qa_video01_decision',
           'qa_video01_rejection_reason',
           'qa_video01_comment',
           'vendor_rating',
           'rating_comment',
           'qa_1_pii',
           'default_avatar',
           '_unit_id',
           '_id',
           '_tainted',
           '_channel',
           '_trust',
           '_country',
           '_region',
           '_city',
           '_ip',
           'qa_video01_comment_gold',
           'rating_comment_gold',
           'vendor_rating_gold'
           ]
qa_report["_started_at"] = pd.to_datetime(qa_report._started_at)
qa_report.sort_values(by="_started_at",inplace=True, ascending=False)
qa_report.drop_duplicates(keep="last",inplace=True,subset="session_name")
qa_report = qa_report[columns]
#show(qa_report)
qa_report.to_csv(targetdir_appen+'\\LarsenaConversation_QA_Report.csv', index=False)