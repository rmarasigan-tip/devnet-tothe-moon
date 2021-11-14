from requests import get


while True: 
    print("Press q or type 'quit' to exit")
    print("---------------------------------------------")
    ip = input("Input IP Address: ")
    if ip == "quit" or ip == "q":
        break
    print("=============================================")
    print("IP: "+ ip) 
    print("City: "+ get('https://ipapi.co/'+ip+'/city').text)
    print("Country: "+get('https://ipapi.co/'+ip+'/country').text)
    print("Timezone: "+ get('https://ipapi.co/'+ip+'/timezone').text)
    print("Country Capital: "+get('https://ipapi.co/'+ip+'/country_capital').text)
    print("Postal Code: "+ get('https://ipapi.co/'+ip+'/postal').text)
    print("Organization: "+get('https://ipapi.co/'+ip+'/org').text)
    print("Language Spoken: "+get('https://ipapi.co/'+ip+'/languages').text)
    print("Country Population: "+get('https://ipapi.co/'+ip+'/country_population').text + " people")
    print("=============================================")

    