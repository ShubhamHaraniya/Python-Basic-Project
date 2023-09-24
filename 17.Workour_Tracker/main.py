from datetime import datetime
import requests
APP_ID = "2ed867b8"
APP_KEY = "b5752ee5bbd4d30d65104ed406cf569e"
Gender = "male"
Weight = 82
Height = 182
Age = 18
Nutritionix_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
Header = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
}
exercisea_text = input("Tell me which exercise you did: ") 
parameters = {
    "query":exercisea_text,
    "gender":Gender,
    "weight_kg": Weight,
    "height_cm": Height,
    "age": Age
}
responses = requests.post(url = Nutritionix_Endpoint,json=parameters,headers=Header)
data = responses.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheety_endpoint = "https://api.sheety.co/ee669da26ba75dd404d24a6d38eb26ac/myWorkOut/workouts"
for exercise in data['exercises']:
    sheet_input = {
        "workout" : {
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise['user_input'],
            "duration" : str(exercise['duration_min']),
            "calories" : exercise['nf_calories'],
        }
    }
    res = requests.post(url=sheety_endpoint,json=sheet_input)
    print(res.text)