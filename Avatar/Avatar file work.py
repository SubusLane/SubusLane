import pandas as pd


cols = ["session_name","accuracy_anger","accuracy_blink","accuracy_disgust","accuracy_eyebrows","accuracy_fear",
        "accuracy_furrow","accuracy_happiness","accuracy_look_up_and_rotate",
        "accuracy_look_up_and_rotate_head_counterclockwise","accuracy_open_mouth","accuracy_sadness",
        "accuracy_smile_lips","accuracy_squint","accuracy_surprise","accuracy_tilt_head_left","accuracy_tilt_head_right",
        "accuracy_turn_head_left","accuracy_turn_head_right","accuracy_widen","comfortibility_anger",
        "comfortibility_blink","comfortibility_disgust","comfortibility_eyebrows","comfortibility_fear",
        "comfortibility_furrow","comfortibility_happiness","comfortibility_look_up_and_rotate",
        "comfortibility_look_up_and_rotate_head_counterclockwise","comfortibility_open_mouth",
        "comfortibility_sadness","comfortibility_smile_lips","comfortibility_squint","comfortibility_surprise",
        "comfortibility_tilt_head_left","comfortibility_tilt_head_right","comfortibility_turn_head_left",
        "comfortibility_turn_head_right","comfortibility_widen","expressivity_anger","expressivity_blink",
        "expressivity_disgust","expressivity_eyebrows","expressivity_fear","expressivity_furrow","expressivity_happiness",
        "expressivity_look_up_and_rotate","expressivity_look_up_and_rotate_head_counterclockwise","expressivity_open_mouth",
        "expressivity_sadness","expressivity_smile_lips","expressivity_squint","expressivity_surprise",
        "expressivity_tilt_head_left","expressivity_tilt_head_right","expressivity_turn_head_left",
        "expressivity_turn_head_right","expressivity_widen","reactivity_anger_fc","reactivity_blink_fc","reactivity_disgust_fc","reactivity_eyebrows_fc","reactivity_fear_fc",
        "reactivity_furrow_fc","reactivity_happiness_fc","reactivity_look_up_and_rotate_fc",
        "reactivity_look_up_and_rotate_head_counterclockwise_fc","reactivity_open_mouth_fc","reactivity_sadness_fc",
        "reactivity_smile_lips_fc","reactivity_squint_fc","reactivity_surprise_fc","reactivity_tilt_head_left_fc",
        "reactivity_tilt_head_right_fc","reactivity_turn_head_left_fc","reactivity_turn_head_right_fc",
        "reactivity_widen_fc","stability_anger_fc","stability_blink_fc","stability_disgust_fc","stability_eyebrows_fc",
        "stability_fear_fc","stability_furrow_fc","stability_happiness_fc","stability_look_up_and_rotate_fc",
        "stability_look_up_and_rotate_head_counterclockwise_fc","stability_open_mouth_fc","stability_sadness_fc",
        "stability_smile_lips_fc","stability_squint_fc","stability_surprise_fc","stability_tilt_head_left_fc",
        "stability_tilt_head_right_fc","stability_turn_head_left_fc","stability_turn_head_right_fc","stability_widen_fc",
        "thinking_about_your_experience_with_the_avatar_today_how_would_you_rate_its_performance","os_option",
        "messenger_option"]

delivery_input = pd.read_csv("C:\\Users\\subha\\Desktop\\Appen\\Avatar file work\\session_stat.csv")

delivery_input["accuracy_furrow"]=delivery_input.accuracy_furrow.fillna(0)+delivery_input.accuracy__furrow_fc.fillna(0)
delivery_input["accuracy_anger"]=delivery_input.accuracy_anger.fillna(0)+delivery_input.accuracy_anger_fc.fillna(0)
delivery_input["accuracy_blink"]=delivery_input.accuracy_blink.fillna(0)+delivery_input.accuracy_blink_fc.fillna(0)
delivery_input["accuracy_disgust"]=delivery_input.accuracy_disgust.fillna(0)+delivery_input.accuracy_disgust_fc.fillna(0)
delivery_input["accuracy_eyebrows"]=delivery_input.accuracy_eyebrows.fillna(0)+delivery_input.accuracy_eyebrows_fc.fillna(0)
delivery_input["accuracy_fear"]=delivery_input.accuracy_fear.fillna(0)+delivery_input.accuracy_fear_fc.fillna(0)
delivery_input["accuracy_happiness"]=delivery_input.accuracy_happiness.fillna(0)+delivery_input.accuracy_happiness_fc.fillna(0)
delivery_input["accuracy_look_up_and_rotate"]=delivery_input.accuracy_look_up_and_rotate.fillna(0)+delivery_input.accuracy_look_up_and_rotate_fc.fillna(0)
delivery_input["accuracy_look_up_and_rotate_head_counterclockwise"]=delivery_input.accuracy_look_up_and_rotate_head_counterclockwise.fillna(0)+delivery_input.accuracy_look_up_and_rotate_head_counterclockwise_fc.fillna(0)
delivery_input["accuracy_open_mouth"]=delivery_input.accuracy_open_mouth.fillna(0)+delivery_input.accuracy_open_mouth_fc.fillna(0)
delivery_input["accuracy_sadness"]=delivery_input.accuracy_sadness.fillna(0)+delivery_input.accuracy_sadness_fc.fillna(0)
delivery_input["accuracy_smile_lips"]=delivery_input.accuracy_smile_lips.fillna(0)+delivery_input.accuracy_smile_lips_fc.fillna(0)
delivery_input["accuracy_squint"]=delivery_input.accuracy_squint.fillna(0)+delivery_input.accuracy_squint_fc.fillna(0)
delivery_input["accuracy_surprise"]=delivery_input.accuracy_surprise.fillna(0)+delivery_input.accuracy_surprise_fc.fillna(0)
delivery_input["accuracy_tilt_head_left"]=delivery_input.accuracy_tilt_head_left.fillna(0)+delivery_input.accuracy_tilt_head_left_fc.fillna(0)
delivery_input["accuracy_tilt_head_right"]=delivery_input.accuracy_tilt_head_right.fillna(0)+delivery_input.accuracy_tilt_head_right_fc.fillna(0)
delivery_input["accuracy_turn_head_left"]=delivery_input.accuracy_turn_head_left.fillna(0)+delivery_input.accuracy_turn_head_left_fc.fillna(0)
delivery_input["accuracy_turn_head_right"]=delivery_input.accuracy_turn_head_right.fillna(0)+delivery_input.accuracy_turn_head_right_fc.fillna(0)
delivery_input["accuracy_widen"]=delivery_input.accuracy_widen.fillna(0)+delivery_input.accuracy_widen_fc.fillna(0)


delivery_input=delivery_input[cols]
#delevery_input['Name'] = delevery_input[['accuracy__furrow_fc', 'accuracy_furrow']].apply(lambda x: ' '.join(x), axis = 1)
#frame['c'] = frame.a.fillna(0) + frame.b.fillna(0)




delivery_input.to_csv("C:\\Users\\subha\\Desktop\\Appen\\Avatar file work\\delivery_input.csv", index=False)
print("done!")
