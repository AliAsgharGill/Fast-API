from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/about")
async def about() -> dict[str, str]: 
    return {"message": "About"}

# in the following example we will get internal server error because data is not according to the return type
@app.get("/contact")
async def contact() -> list: # return type is list but we need to return dictionary like this: dict[str, str]
    return {"message": "Contact"}