from urllib import response
import apikey

import requests        

API_KEY = apikey.api_key()  

Base_url ="http://api.openweathermap.org/data/2.5/weather"      

while True :
    
    city_name = input("Enter a City Name : ") 
    
    user_need = input("Type to get specific information about : weather  / main / wind / clouds / complete detail / close or quit := ").lower()

    request_url = f"{Base_url}?appid={API_KEY}&q={city_name}"

    response=requests.get(request_url)  

    if response.status_code==200:      
        data = response.json()      

        if user_need == "close" or user_need== "quit" :

            break

        if user_need == "weather" :
            weather1 = data['weather']
            print(weather1)


        elif user_need=="clouds" :

            cloud = data['clouds']
            print(cloud)


        elif user_need=="wind" :
            winds = data['wind']
            print(winds)


        elif user_need=="main" :
            mains = data['main']
            print(mains)


        elif user_need=="complete detail" :
            print(data)


        # elif user_need=="sys" :
        #     syss = data['sys']
        #     print(syss)

  
    else :
        print("An Error Occured.") 

# Done
