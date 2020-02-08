
import requests, json
import urllib.parse
import sys
import time

# Main code : bjspJcEimu4sGO3RXgXNTe5uXlce6DpAB93OZLpfzOQ

# test code : h3JTI0wlvYtpPR6UGlTVMCLe6kBSmnfS3Gmdayr2OAx

LINE_ACCESS_TOKEN = "h3JTI0wlvYtpPR6UGlTVMCLe6kBSmnfS3Gmdayr2OAx"
URL_LINE = "https://notify-api.line.me/api/notify" 

def line_text(message):	
    msg = urllib.parse.urlencode({"message":message})
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    session_post = session.post(URL_LINE, headers=LINE_HEADERS, data=msg)
    print(session_post.text)

def line_pic(message, path_file):
    file_img = {'imageFile': open(path_file, 'rb')}
    msg = ({'message': message})
    LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    session_post = session.post(URL_LINE, headers=LINE_HEADERS, files=file_img, data=msg)
    print(session_post.text)

#test limitation line API

def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

def lineNotify(message):
    payload = {'message':message}
    return _lineNotify2(payload)

def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'bjspJcEimu4sGO3RXgXNTe5uXlce6DpAB93OZLpfzOQ'	#EDIT
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

def _lineNotify2(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'tVoB2zg6fmx5ci6H4kJccTHrRKckBPUQOQdEAepNeX9'	#EDIT
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)
    
    

if __name__ == "__main__":

            line_text("Unit test as of 08/02/2020")
            line_pic("Test", "C:/Users/Gain/Desktop/NewEGAT/123.jpg")
        
        