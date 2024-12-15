"""
Main FastAPI application module.

This module defines basic endpoints for a simple web application.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Root endpoint returning a basic welcome message.

    Returns:
        dict: Dictionary with a welcome message.
    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    Endpoint returning a personalized greeting message.

    Args:
        name (str): Name of the person to greet.

    Returns:
        dict: Dictionary with a greeting message containing the provided name.
    """
    return {"message": f"Hello {name}"}
