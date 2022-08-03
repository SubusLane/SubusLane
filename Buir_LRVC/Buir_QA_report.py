#from pandasgui import show
import pandas as pd
import requests
import os
import time
import zipfile
from datetime import datetime

def get_duplicates(row):
    working = qa_report[qa_report["ac_id"] == row.ac_id]
    working = working[working["session"] != row.session]
    objects_list = working["object"].unique()
    if row.object in objects_list:
        return row.object
    else:
        return "n"


job_id_appen='1905711' #Add job id
targetdir_appen=r'C:\Users\subha\Appen\Falcon Multi Persons Video Collection 2021 - Documents\Buir_LRAC\Reports' #Add folder location
#targetdir_appen=r'C:\Users\subha\Desktop\Buir QA report test'
def get_QAreport(job_id,targetdir):
    job_id = job_id
    targetdir = targetdir
    
    
    headers = {'Authorization': 'Token token=###'}
    data = {'type': 'full'}
    response = requests.post('https://api.appen.com/v1/jobs/'+job_id+'/regenerate', headers=headers, data=data)    
    print(response) #Just for debug
    #os.system(response)
    time.sleep(30)
    data = {'type': 'full'}
    response = requests.get('https://api.appen.com/v1/jobs/'+job_id+'.csv', headers=headers, data=data)   
    print(response) #Just for debug

    targetdir = targetdir

    with open(targetdir+"\\"+job_id+".zip", 'wb') as f:   #Saving the zip locally
        f.write(response.content)
    with zipfile.ZipFile(targetdir+"\\"+job_id +".zip","r") as zip_ref: #Extraction in folder
        zip_ref.extractall(targetdir)
    time.sleep(30)
    #os.remove(targetdir+"\\"+job_id+".zip")


get_QAreport(job_id_appen,targetdir_appen)  #Calling function

qa_report = pd.read_csv(targetdir_appen+"\\f"+job_id_appen+".csv")

qa_report["skin_tone_01"].fillna(qa_report["skin_tone"], inplace=True)
qa_report["skin_tone_02"].fillna(qa_report["skin_tone2"], inplace=True)
qa_report["skin_tone_03"].fillna(qa_report["skin_tone3"], inplace=True)
qa_report["skin_tone"]=qa_report["skin_tone_01"]
qa_report["skin_tone2"]=qa_report["skin_tone_02"]
qa_report["skin_tone3"]=qa_report["skin_tone_03"]

qa_report["orientation_01"].fillna(qa_report["orientation"], inplace=True)
qa_report["orientation_02"].fillna(qa_report["orientation2"], inplace=True)
qa_report["orientation_03"].fillna(qa_report["orientation3"], inplace=True)
qa_report["orientation"]=qa_report["orientation_01"]
qa_report["orientation2"]=qa_report["orientation_02"]
qa_report["orientation3"]=qa_report["orientation_03"]

qa_report["gender_01"].fillna(qa_report["gender"], inplace=True)
qa_report["gender_02"].fillna(qa_report["gender2"], inplace=True)
qa_report["gender_03"].fillna(qa_report["gender3"], inplace=True)
qa_report["gender"]=qa_report["gender_01"]
qa_report["gender2"]=qa_report["gender_02"]
qa_report["gender3"]=qa_report["gender_03"]

qa_report["hair_length_01"].fillna(qa_report["hair_length"], inplace=True)
qa_report["hair_length_02"].fillna(qa_report["hair_length2"], inplace=True)
qa_report["hair_length_03"].fillna(qa_report["hair_length3"], inplace=True)
qa_report["hair_length"]=qa_report["hair_length_01"]
qa_report["hair_length2"]=qa_report["hair_length_02"]
qa_report["hair_length3"]=qa_report["hair_length_03"]

qa_report["hair_style_01"].fillna(qa_report["hair_style"], inplace=True)
qa_report["hair_style_02"].fillna(qa_report["hair_style2"], inplace=True)
qa_report["hair_style_03"].fillna(qa_report["hair_style3"], inplace=True)
qa_report["hair_style"]=qa_report["hair_style_01"]
qa_report["hair_style2"]=qa_report["hair_style_02"]
qa_report["hair_style3"]=qa_report["hair_style_03"]

qa_report["hair_color_01"].fillna(qa_report["hair_color"], inplace=True)
qa_report["hair_color_02"].fillna(qa_report["hair_color2"], inplace=True)
qa_report["hair_color_03"].fillna(qa_report["hair_color3"], inplace=True)
qa_report["hair_color"]=qa_report["hair_color_01"]
qa_report["hair_color2"]=qa_report["hair_color_02"]
qa_report["hair_color3"]=qa_report["hair_color_03"]

columns = [
            "_unit_id",
            "_created_at",
            "_id",
            "_started_at",
            "_tainted",
            "_channel",
            "_trust",
            "_worker_id",
            "_country",
            "_region",
            "_city",
            "_ip",
            "directory_name",
            "pin",
            "script_name",
            "script_num",
            "qa_pass_video_dance_01",
            "qa_pass_video_dance_02",
            "qa_pass_video_dance_03",
            "rejection_reason_01",
            "rejection_reason_02",
            "rejection_reason_03",
            "input_comment_qa_dance_01",
            "input_comment_qa_dance_02",
            "input_comment_qa_dance_03",
            "input_comment_metadata",
            "input_comment_metadata2",
            "input_comment_metadata3",
            "number_of_people1",
            "number_of_people2",
            "number_of_people3",
            "background_uniformity_video_dance_01",
            "background_uniformity_video_dance_02",
            "background_uniformity_video_dance_03",
            "scenery_video_dance_01",
            "scenery_video_dance_02",
            "scenery_video_dance_03",
            "lighting_video_dance_01",
            "lighting_video_dance_02",
            "lighting_video_dance_03",
            "subject_exposure_dance_01",
            "subject_exposure_dance_02",
            "subject_exposure_dance_03",
            "people_seen_in_background",
            "people_seen_in_background2",
            "people_seen_in_background3",
            "pets_seen_in_foreground",
            "pets_seen_in_foreground2",
            "pets_seen_in_foreground3",
            "type",
            "type2",
            "type3",
            "device_model",
            "orientation",
            "orientation2",
            "orientation3",
            "camera_setting1",
            "camera_setting2",
            "camera_setting3",
            "skin_tone",
            "skin_tone2",
            "skin_tone3",
            "skin_tone_01",
            "skin_tone_02",
            "skin_tone_03",
            "gender",
            "gender2",
            "gender3",
            "gender_01",
            "gender_02",
            "gender_03",
            "age",
            "age2",
            "age3",
            "hair_length",
            "hair_length2",
            "hair_length3",
            "hair_length_01","hair_length_02","hair_length_03",
            "hair_style",
            "hair_style2",
            "hair_style3",
            "hair_style_01","hair_style_02","hair_style_03",
            "hair_color",
            "hair_color2",
            "hair_color3",
            "hair_color_01","hair_color_02","hair_color_03",
            "beard_length_dance_01",
            "beard_length_dance_02",
            "beard_length_dance_03",
            "v2_beard_length_01",
            "v2_beard_length_02",
            "v2_beard_length_03",
            "v3_beard_length_01",
            "v3_beard_length_02",
            "v3_beard_length_03",
            "beard_color_01",
            "beard_color_02",
            "beard_color_03",
            "v2_beard_color_01",
            "v2_beard_color_02",
            "v2_beard_color_03",
            "v3_beard_color_01",
            "v3_beard_color_02",
            "v3_beard_color_03",
            "visible_tattoos_01",
            "visible_tattoos_02",
            "visible_tattoos_03",
            "v2_visible_tattoos_01",
            "v2_visible_tattoos_02",
            "v2_visible_tattoos_03",
            "v3_visible_tattoos_01",
            "v3_visible_tattoos_02",
            "v3_visible_tattoos_03",
            "eyebrows_thickness_01",
            "eyebrows_thickness_02",
            "eyebrows_thickness_03",
            "v2_eyebrows_thickness_01",
            "v2_eyebrows_thickness_02",
            "v2_eyebrows_thickness_03",
            "v3_eyebrows_thickness_01",
            "v3_eyebrows_thickness_02",
            "v3_eyebrows_thickness_03",
            "eyebrows_style_01",
            "eyebrows_style_02",
            "eyebrows_style_03",
            "v2_eyebrows_style_01",
            "v2_eyebrows_style_02",
            "v2_eyebrows_style_03",
            "v3_eyebrows_style_01",
            "v3_eyebrows_style_02",
            "v3_eyebrows_style_03",
            "eyes_color_01",
            "eyes_color_02",
            "eyes_color_03",
            "v2_eyes_color_01",
            "v2_eyes_color_02",
            "v2_eyes_color_03",
            "v3_eyes_color_01",
            "v3_eyes_color_02",
            "v3_eyes_color_03",
            "eyes_shape_01",
            "eyes_shape_02",
            "eyes_shape_03",
            "v2_eyes_shape_01",
            "v2_eyes_shape_02",
            "v2_eyes_shape_03",
            "v3_eyes_shape_01",
            "v3_eyes_shape_02",
            "v3_eyes_shape_03",
            "eyes_direction_01",
            "eyes_direction_02",
            "eyes_direction_03",
            "v2_eyes_direction_01",
            "v2_eyes_direction_02",
            "v2_eyes_direction_03",
            "v3_eyes_direction_01",
            "v3_eyes_direction_02",
            "v3_eyes_direction_03",
            "eyes_size_01",
            "eyes_size_02",
            "eyes_size_03",
            "v2_eyes_size_01",
            "v2_eyes_size_02",
            "v2_eyes_size_03",
            "v3_eyes_size_01",
            "v3_eyes_size_02",
            "v3_eyes_size_03",
            "eye_lids_type_01",
            "eye_lids_type_02",
            "eye_lids_type_03",
            "v2_eye_lids_type_01",
            "v2_eye_lids_type_02",
            "v2_eye_lids_type_03",
            "v3_eye_lids_type_01",
            "v3_eye_lids_type_02",
            "v3_eye_lids_type_03",
            "nose_shape_01",
            "nose_shape_02",
            "nose_shape_03",
            "v2_nose_shape_01",
            "v2_nose_shape_02",
            "v2_nose_shape_03",
            "v3_nose_shape_01",
            "v3_nose_shape_02",
            "v3_nose_shape_03",
            "nose_size_01",
            "nose_size_02",
            "nose_size_03",
            "v2_nose_size_01",
            "v2_nose_size_02",
            "v2_nose_size_03",
            "v3_nose_size_01",
            "v3_nose_size_02",
            "v3_nose_size_03",
            "lip_shape_01",
            "lip_shape_02",
            "lip_shape_03",
            "v2_lip_shape_01",
            "v2_lip_shape_02",
            "v2_lip_shape_03",
            "v3_lip_shape_01",
            "v3_lip_shape_02",
            "v3_lip_shape_03",
            "lip_size_01",
            "lip_size_02",
            "lip_size_03",
            "v2_lip_size_01",
            "v2_lip_size_02",
            "v2_lip_size_03",
            "v3_lip_size_01",
            "v3_lip_size_02",
            "v3_lip_size_03",
            "over_ear_headphones_01",
            "over_ear_headphones_02",
            "over_ear_headphones_03",
            "v2_over_ear_headphones_01",
            "v2_over_ear_headphones_02",
            "v2_over_ear_headphones_03",
            "v3_over_ear_headphones_01",
            "v3_over_ear_headphones_02",
            "v3_over_ear_headphones_03",
            "in_ear_headphones_01",
            "in_ear_headphones_02",
            "in_ear_headphones_03",
            "v2_in_ear_headphones_01",
            "v2_in_ear_headphones_02",
            "v2_in_ear_headphones_03",
            "v3_in_ear_headphones_01",
            "v3_in_ear_headphones_02",
            "v3_in_ear_headphones_03",
            "wearing_mask_01",
            "wearing_mask_02",
            "wearing_mask_03",
            "v2_wearing_mask_01",
            "v2_wearing_mask_02",
            "v2_wearing_mask_03",
            "v3_wearing_mask_01",
            "v3_wearing_mask_02",
            "v3_wearing_mask_03",
            "glasses_style_01",
            "glasses_style_02",
            "glasses_style_03",
            "v2_glasses_style_01",
            "v2_glasses_style_02",
            "v2_glasses_style_03",
            "v3_glasses_style_01",
            "v3_glasses_style_02",
            "v3_glasses_style_03",
            "glasses_frames_01",
            "glasses_frames_02",
            "glasses_frames_03",
            "v2_glasses_frames_01",
            "v2_glasses_frames_02",
            "v2_glasses_frames_03",
            "v3_glasses_frames_01",
            "v3_glasses_frames_02",
            "v3_glasses_frames_03",
            "glasses_lens_01",
            "glasses_lens_02",
            "glasses_lens_03",
            "v2_glasses_lens_01",
            "v2_glasses_lens_02",
            "v2_glasses_lens_03",
            "v3_glasses_lens_01",
            "v3_glasses_lens_02",
            "v3_glasses_lens_03",
            "wearing_headwear_01",
            "wearing_headwear_02",
            "wearing_headwear_03",
            "v2_wearing_headwear_01",
            "v2_wearing_headwear_02",
            "v2_wearing_headwear_03",
            "v3_wearing_headwear_01",
            "v3_wearing_headwear_02",
            "v3_wearing_headwear_03",
            "wearing_single_clothing_piece_01",
            "wearing_single_clothing_piece_02",
            "wearing_single_clothing_piece_03",
            "v2_wearing_single_clothing_piece_01",
            "v2_wearing_single_clothing_piece_02",
            "v2_wearing_single_clothing_piece_03",
            "v3_wearing_single_clothing_piece_01",
            "v3_wearing_single_clothing_piece_02",
            "v3_wearing_single_clothing_piece_03",
            "clothing_matches_bg_01",
            "clothing_matches_bg_02",
            "clothing_matches_bg_03",
            "v2_clothing_matches_bg_01",
            "v2_clothing_matches_bg_02",
            "v2_clothing_matches_bg_03",
            "v3_clothing_matches_bg_01",
            "v3_clothing_matches_bg_02",
            "v3_clothing_matches_bg_03",
            "top_clothing_fit_01",
            "top_clothing_fit_02",
            "top_clothing_fit_03",
            "v2_top_clothing_fit_01",
            "v2_top_clothing_fit_02",
            "v2_top_clothing_fit_03",
            "v3_top_clothing_fit_01",
            "v3_top_clothing_fit_02",
            "v3_top_clothing_fit_03",
            "bottom_clothing_fit_01",
            "bottom_clothing_fit_02",
            "bottom_clothing_fit_03",
            "v2_bottom_clothing_fit_01",
            "v2_bottom_clothing_fit_02",
            "v2_bottom_clothing_fit_03",
            "v3_bottom_clothing_fit_01",
            "v3_bottom_clothing_fit_02",
            "v3_bottom_clothing_fit_03",
            "holding_sign_01",
            "holding_sign_02",
            "holding_sign_03",
            "v2_holding_sign_01",
            "v2_holding_sign_02",
            "v2_holding_sign_03",
            "v3_holding_sign_01",
            "v3_holding_sign_02",
            "v3_holding_sign_03",
            "holding_phone_01",
            "holding_phone_02",
            "holding_phone_03",
            "v2_holding_phone_01",
            "v2_holding_phone_02",
            "v2_holding_phone_03",
            "v3_holding_phone_01",
            "v3_holding_phone_02",
            "v3_holding_phone_03",
            "hands_are_moving_01",
            "hands_are_moving_02",
            "hands_are_moving_03",
            "v2_hands_are_moving_01",
            "v2_hands_are_moving_02",
            "v2_hands_are_moving_03",
            "v3_hands_are_moving_01",
            "v3_hands_are_moving_02",
            "v3_hands_are_moving_03",
            "hands_stretched_01",
            "hands_stretched_02",
            "hands_stretched_03",
            "v2_hands_stretched_01",
            "v2_hands_stretched_02",
            "v2_hands_stretched_03",
            "v3_hands_stretched_01",
            "v3_hands_stretched_02",
            "v3_hands_stretched_03",
            "pose_01",
            "pose_02",
            "pose_03",
            "v2_pose_01",
            "v2_pose_02",
            "v2_pose_03",
            "v3_pose_01",
            "v3_pose_02",
            "v3_pose_03",
            "sitting_or_standing_01",
            "sitting_or_standing_02",
            "sitting_or_standing_03",
            "v2_sitting_or_standing_01",
            "v2_sitting_or_standing_02",
            "v2_sitting_or_standing_03",
            "v3_sitting_or_standing_01",
            "v3_sitting_or_standing_02",
            "v3_sitting_or_standing_03",
            "screen_moving_with_person_01",
            "screen_moving_with_person_02",
            "screen_moving_with_person_03",
            "v2_screen_moving_with_person_01",
            "v2_screen_moving_with_person_02",
            "v2_screen_moving_with_person_03",
            "v3_screen_moving_with_person_01",
            "v3_screen_moving_with_person_02",
            "v3_screen_moving_with_person_03",
            "performing_activity_01",
            "performing_activity_02",
            "performing_activity_03",
            "v2_performing_activity_01",
            "v2_performing_activity_02",
            "v2_performing_activity_03",
            "v3_performing_activity_01",
            "v3_performing_activity_02",
            "v3_performing_activity_03",
            "single_person_comment",
            "two_person_comment",
            "three_person_comment",
            "video_01_url",
            "video_02_url",
            "video_03_url",
            "activity_01",
            "activity_02",
            "activity_03"
           ]

qa_report["_started_at"] = pd.to_datetime(qa_report._started_at)
qa_report.sort_values(by="_started_at",inplace=True, ascending=False)
qa_report.drop_duplicates(keep="last",inplace=True,subset="directory_name")
qa_report = qa_report[columns]
qa_report.rename(columns={"qa_pass_video_dance_01": "qa_decesion_daily_act", 
                   "qa_pass_video_dance_02": "qa_decesion_walk",
                   "qa_pass_video_dance_03": "qa_decesion_dance",
                   "input_comment_qa_dance_01":"input_comment_daily_act",
                    "input_comment_qa_dance_02":"input_comment_qa_walk",
                    "input_comment_qa_dance_03":"input_comment_qa_dance",
                    "background_uniformity_video_dance_01":"background_uniformity_video_daily_act",
                    "background_uniformity_video_dance_02":"background_uniformity_video_walk",
                    "background_uniformity_video_dance_03":"background_uniformity_video_dance",
                    "scenery_video_dance_01":"scenery_video_daily_act",
                    "scenery_video_dance_02":"scenery_video_walk",
                    "scenery_video_dance_03":"scenery_video_dance",
                    "lighting_video_dance_01":"lighting_video_daily_act",
                    "lighting_video_dance_02":"lighting_video_walk",
                    "lighting_video_dance_03":"lighting_video_dance",
                    "subject_exposure_dance_01":"subject_exposure_daily_act",
                    "subject_exposure_dance_02":"subject_exposure_walk:",
                    "subject_exposure_dance_03":"subject_exposure_dance"}, inplace=True)
#show(qa_report)
qa_report.to_csv(targetdir_appen+'\\Buir_LRAC_QA_Report.csv', index=False)
qa_report.to_csv(targetdir_appen+'\\Buir_LRAC_QA_Report.xlsx', index=False)
# datetime object containing current date and time
now = datetime.now()
#print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
print("-End-")
