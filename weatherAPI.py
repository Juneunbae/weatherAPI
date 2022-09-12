import requests
import json

city = 'Seoul'
info = '''
1. Seoul
2. Busan
3. Incheon
'''
print(info)

inputVal = input("번호를 입력하세요 : ")

if int(inputVal) == 2 :
    city = "Busan"
elif int(inputVal) == 3 :
    city = "Incheon"
else :
    city = 'Seoul'


response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=14cb3ed146a04e5f8f9152308221209&\
                        q={city}&api=yes')
jsonObj = json.loads(response.text)
json.dumps(jsonObj, indent=4)

print(f"{city}의 기온은 {jsonObj['current']['temp_c']}, {city}의 기상상태는 {jsonObj['current']['condition']['text']}")