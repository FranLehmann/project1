import test1
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def getSource():
    return [1,2,3,4,5,6,7,8,9]
@app.get('/contact')
def getSource():
    return {'name':'Franco'}
def run():
    return test1.getProducts()


if __name__ == '__main__':
    run()

