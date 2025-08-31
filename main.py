from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def HelloWorld():
    a = 10 
    b = 10
    return a