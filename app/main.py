from random import gauss

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Goodbye": "You"}


@app.get("/get_prediction")
def get_prediction(feature_a: float, feature_b: float):
    return {"prediction": gauss(mu=feature_a, sigma=feature_b)}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
