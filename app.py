from fastapi import FastAPI
import random
import time

app = FastAPI()

@app.get("/api/random")
async def get_random():
    # Simulate random response times between 100ms and 3 seconds
    delay = random.uniform(0.1, 3)
    time.sleep(delay)
    return {"message": "Success", "response_time": f"{delay:.2f} seconds"}
