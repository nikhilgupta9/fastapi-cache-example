# Importing the required packages
import requests
import redis
import json
from fastapi import FastAPI

# Instances
rd = redis.Redis(host="database", port=6379, db=0)
app = FastAPI()

# Health check
@app.get("/")
def read_root():
  return "Hello World"

# Square of a number
@app.get("/square/{number}")
def square(number: int):
  cache = rd.get(number)
  if cache:
    print("cache hit")
    return cache
  else:
    print("cache miss")
    rd.set(number, number ** 2)
    rd.expire(number, 120)
    return number ** 2