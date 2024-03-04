import requests

def getProducts():
    try:
        req = requests.get('https://api.escuelajs.co/api/v1/products')
        print(req)
        print(req.status_code)
        print(req.text)


    except:
        raise Exception('Dosen`t find the resource.')
