import os
import sys
import urllib.request
client_id = "bh51u91nlo"
client_secret = "0zRDttwNbszDNeBMgBrzJsSmmOPtZDRzr6du9Hst"
encText = urllib.parse.quote("반갑습니다 네이버")
data = "speaker=nara&volume=0&speed=0&pitch=0&emotion=0&format=mp3&text=" + encText;
url = "https://naveropenapi.apigw.ntruss.com/voice-premium/v1/tts"
request = urllib.request.Request(url)
request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
request.add_header("X-NCP-APIGW-API-KEY",client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('1111.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)