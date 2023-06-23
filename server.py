from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from backoffice"}

def callback(ch, method, properties, body):
    pass

def main():
    print("\\ main function called \\")

@app.on_event("startup")
def on_startup():
    # create helper object to handle messages from rabbitmq
    main()

@app.on_event("shutdown")
async def on_shutdown():
    # shutdown rabbitmq
    pass