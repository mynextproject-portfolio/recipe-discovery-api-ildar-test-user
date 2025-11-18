from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping():
    """Health check endpoint to verify the service is running."""
    return "pong"

