from tkinter import E
from fastapi import FastAPI
import os
import sentry_sdk

app = FastAPI()

sentry_dsn = os.getenv("SENTRY_DSN")
if sentry_dsn is None:
    raise ValueError("No SENTRY_DSN environment variable set")

sentry_sdk.init(
    dsn=sentry_dsn,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)


@app.get("/error/explicit")
async def explicit_error():
    raise Exception("This is an explicit test error")


@app.get("/error/implicit")
async def implicit_error():
    div = 1 / 0