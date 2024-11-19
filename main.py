from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class GenreURLChoices(Enum):
    Rock = "rock"
    Hard_Rock = "hard rock"
    Progressive_Rock = "progressive rock"
    Classic_Rock = "classic rock"
    Grunge = "grunge"
    Metal = "metal"
    Alternative_Rock = "alternative rock"
    Punk_Rock = "punk rock"
    Pop_Rock = "pop rock"
    Indie_Rock = "indie rock"

BANDS = [
  {
    "id": 1,
    "name": "The Beatles",
    "genre": "Rock"
  },
  {
    "id": 2,
    "name": "Led Zeppelin",
    "genre": "Hard Rock"
  },
  {
    "id": 3,
    "name": "Pink Floyd",
    "genre": "Progressive Rock"
  },
  {
    "id": 4,
    "name": "Queen",
    "genre": "Classic Rock"
  },
  {
    "id": 5,
    "name": "Nirvana",
    "genre": "Grunge"
  },
  {
    "id": 6,
    "name": "Metallica",
    "genre": "Metal"
  },
  {
    "id": 7,
    "name": "Radiohead",
    "genre": "Alternative Rock"
  },
  {
    "id": 8,
    "name": "Green Day",
    "genre": "Punk Rock"
  },
  {
    "id": 9,
    "name": "Coldplay",
    "genre": "Pop Rock"
  },
  {
    "id": 10,
    "name": "Imagine Dragons",
    "genre": "Indie Rock"
  },
  {
    "id": 1,
    "name": "The New Beatles",
    "genre": "Rock"
  },
]


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

@app.get("/bands")
async def bands() -> list[dict]:
    return BANDS

# Path Parameters
# we can also give specific status code parameter to the request like here 
# @app.get("/bands/{band_id}")
@app.get("/bands/{band_id}")
async def band(band_id: int) -> dict:
    band = next((band_ for band_ in BANDS if band_["id"] == band_id), None) # This is next(generator comprehension, default), next is built-in function
    if band:
        return band
    raise HTTPException(status_code=404, detail="Band not found")

# Like the following example we can get category of bands
@app.get("/bands/genre/{genre}")
async def bands_by_genre(genre: GenreURLChoices) -> list[dict]:
    # first we were using the following when getting the category of bands without Enum.
    # return [band_ for band_ in BANDS if band_["genre"].lower() == genre.lower()] # This is list comprehension

    # but after enum we are using the following
    return [band_ for band_ in BANDS if band_["genre"].lower() == genre.value] # We change it from lower() to value to get the category of bands with Enum. This is list comprehension