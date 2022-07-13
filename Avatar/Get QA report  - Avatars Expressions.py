import pandas as pd
import requests
import os
import time
import zipfile
import glob

def get_duplicates(row):
    working = qa_report[qa_report["ac_id"] == row.ac_id]
    working = working[working["session"] != row.session]
    objects_list = working["object"].unique()
    if row.object in objects_list:
        return row.object
    else:
        return "n"

job_id_appen='1825113' #Add job id

targetdir_appen=r'C:\Users\subha\Appen\Falcon Messenger Avatars Testing 2021 - Documents\General\Data Collection\01 Tracker\Reports' #Add folder location
#targetdir_appen=r'C:\Users\subha\Desktop\Test avatar API'
def get_QAreport(job_id,targetdir):
    job_id = job_id
    targetdir = targetdir
  
    headers = {'Authorization': 'Token token=pvgbMxCLGsS72ZwsnuYj'}
    data = {'type': 'full'}
    response = requests.post('https://api.appen.com/v1/jobs/'+job_id+'/regenerate', headers=headers, data=data)    
    print(response) #Just for debug
    #os.system(response)
    time.sleep(20)  
    data = {'type': 'full'}
    response = requests.get('https://api.appen.com/v1/jobs/'+job_id+'.csv', headers=headers, data=data)   
    print(response) #Just for debug
    #os.system(response)
    targetdir = targetdir
    with open(targetdir+"/"+job_id+".zip", 'wb') as f:   #Saving the zip locally
        f.write(response.content)
    with zipfile.ZipFile(targetdir+"\\"+job_id +".zip","r") as zip_ref: #Extraction in folder
        zip_ref.extractall(targetdir)
    #time.sleep(10)
    #os.remove(job_id+".zip")

get_QAreport(job_id_appen,targetdir_appen)  #Calling function

#organising file
qa_report = pd.read_csv(targetdir_appen+"\\f"+job_id_appen+".csv")
columns = ['_unit_id',
           '_started_at',
           '_worker_id',
           'ac_id',
           'session_name',
           'default_avatar',
           'debug_avatar',
           'qa_1_pii',
           'qa_2_pii',
           'qa_3_pii',
           'qa_video01_decision',
           'qa_video01_rejection_reason',
           'qa_video01_comment',
           'qa_video02_decision',
           'qa_video02_rejection_reason',
           'qa_video02_comment',
           'qa_video03_decision',
           'qa_video3_rejection_reason',
           'qa_video03_comment',
           'vendor_rating',
           'rating_comment',
           'squint',
           'smile_with_your_lips_and_cheeks_raised',
           'furrow_your_brows_inward',
           'widen_your_eyes',
           'open_your_mouth_gently',
           'raise_your_eyebrows',
           'sadness',
           'happiness',
           'anger',
           'blink',
           'disgust',
           'fear',
           'surprise',
           'tilt_head_left_towards_shoulder',
           'tilt_head_right_towards_shoulder',
           'turn_head_left_show_right_cheek',
           'turn_head_right_show_left_cheek',
           'look_up_and_rotate_head_clockwise',
           'look_up_and_rotate_head_counterclockwise',
           'video01_s3',
           'video02_s3',
           'video03_s3']
qa_report["_started_at"] = pd.to_datetime(qa_report._started_at)
qa_report.sort_values(by="_started_at",inplace=True)
qa_report.drop_duplicates(keep="last",inplace=True,subset="session_name")
qa_report = qa_report[columns]
qa_report.to_csv(targetdir_appen+'\\LuptonExpressions_QA_Report.csv', index=False)

#New QA file after changes
job_id_appen_new="1947781"
get_QAreport(job_id_appen_new,targetdir_appen) 
#organising file
qa_report = pd.read_csv(targetdir_appen+"\\f"+job_id_appen_new+".csv")
columns = ['_unit_id',
           '_started_at',
           '_worker_id',
           'ac_id',
           'session_name',
           'default_avatar',
           'debug_avatar',
           'qa_1_pii',
           'qa_2_pii',
           'qa_3_pii',
           'qa_video01_decision',
           'qa_video01_rejection_reason',
           'qa_video01_comment',
           'qa_video02_decision',
           'qa_video02_rejection_reason',
           'qa_video02_comment',
           'qa_video03_decision',
           'qa_video3_rejection_reason',
           'qa_video03_comment',
           'vendor_rating',
           'rating_comment',
           'squint',
           'smile_with_your_lips_and_cheeks_raised',
           'furrow_your_brows_inward',
           'widen_your_eyes',
           'open_your_mouth_gently',
           'raise_your_eyebrows',
           'sadness',
           'happiness',
           'anger',
           'blink',
           'disgust',
           'fear',
           'surprise',
           'tilt_head_left_towards_shoulder',
           'tilt_head_right_towards_shoulder',
           'turn_head_left_show_right_cheek',
           'turn_head_right_show_left_cheek',
           'look_up_and_rotate_head_clockwise',
           'look_up_and_rotate_head_counterclockwise',
           'video01_s3',
           'video02_s3',
           'video03_s3']
qa_report["_started_at"] = pd.to_datetime(qa_report._started_at)
qa_report.sort_values(by="_started_at",inplace=True)
qa_report.drop_duplicates(keep="last",inplace=True,subset="session_name")
qa_report = qa_report[columns]
qa_report.to_csv(targetdir_appen+'\\new_LuptonExpressions_QA_Report.csv', index=False)

##Marging old and new QA file

# setting the path for joining multiple files
files = os.path.join(targetdir_appen, "*LuptonExpressions_QA_Report.csv")

# list of merged files returned
files = glob.glob(files)

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df["_started_at"] = pd.to_datetime(df._started_at)
#print(df)
df.to_csv(targetdir_appen+"\\LuptonExpressions_QA_Report.csv", index=False)

#####End of file marging

