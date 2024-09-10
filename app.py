import requests
from fastapi import FastAPI
import os

app = FastAPI()

# Set external API URLs (can be set through environment variables)
EXTERNAL_API_1 = os.getenv('EXTERNAL_API_1', 'http://mockoon:3001/api/data1')
EXTERNAL_API_2 = os.getenv('EXTERNAL_API_2', 'http://mockoon:3002/api/data2')

@app.get("/api/orchestrate")
async def orchestrate():
    # Call the first external API
    response1 = requests.get(EXTERNAL_API_1)
    data1 = response1.json()

    # Call the second external API
    response2 = requests.get(EXTERNAL_API_2)
    data2 = response2.json()

    return {
        "message": "Orchestration successful",
        "external_data1": data1,
        "external_data2": data2
    }
