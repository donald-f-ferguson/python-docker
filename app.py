from fastapi import FastAPI
import uvicorn
import os

# We will use this environment variable to "demonstrate" where the application is running.
#
where_am_i = os.environ.get("WHEREAMI", None)
app = FastAPI()

@app.get('/')
def hello_world():
    global where_am_i

    if where_am_i is None:
        where_am_i = "NOT IN DOCKER"

    return f'Hello, from {where_am_i}! I changed.'


if __name__ == "__main__":
    uvicorn.run(app=app, host='0.0.0.0', port=5002)