Create virtual environment using the following command

```
    python -m venv venv
```

then access the virtual environment by activating the following command

```
source venv/bin/activate
```

Install fastapi using the following command

```
pip install fastapi
```

Run the following command

```
pip install -U pip
```

now install uvicorn standard package

```
pip install "uvicorn[standard]"
``
```

then create main.py folder in the root folder of the project

```
    from fastapi import FastAPI
```

create some methods in main.py like the following:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index() -> dict[str, str]:
    return {"message": "Hello World"}

@app.get("/about")
async def about() -> dict[str, str]:
    return {"message": "About"}
```

Run the following command for running on localhost:

```
uvicorn main:app --reload --port 8080
```

we will get internal server errors if data is not accordingly then return type.

Just write "/docs" after running the localhost server for getting api docs.
