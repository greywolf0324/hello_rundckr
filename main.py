import runpod
import os
from dotenv import load_dotenv
import json

load_dotenv()

def is_even(job):

    job_input = job["input"]
    the_number = job_input["number"]

    if not isinstance(the_number, int):
        return {"error": "Silly human, you need to pass an integer."}

    if the_number % 2 == 0:
        return True
    
    return False


# runpod.serverless.start({"handler": is_even})

runpod.api_key = os.getenv("RUNPOD_API_KEY")

gpus = runpod.get_gpus()

print(json.dumps(gpus, indent=2))