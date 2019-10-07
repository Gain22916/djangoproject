import requests



def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'bjspJcEimu4sGO3RXgXNTe5uXlce6DpAB93OZLpfzOQ'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)


def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

def notifyPicture(url):
    payload = {'message':" test123 ", 'imageFile': url }
    return _lineNotify(payload)




if __name__ == '__main__':

    lineNotify('Detect Intruder')
    lineNotify('Raccoon')
    lineNotify('IP camera = 5')
    notifyPicture('imageFile=@D:\Temp\Personal Photo.png')





