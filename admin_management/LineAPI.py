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





