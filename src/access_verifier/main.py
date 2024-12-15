"""
This module provides an API for access verification.

It includes the following functionality:
- Integration with the verification router from the access verifier module.
- A root endpoint that provides a welcome message.

Routes:
- /api/v1: Routes from the verification router are prefixed with /api/v1
- /: A root endpoint that returns a welcome message.
"""
from fastapi import FastAPI
from src.access_verifier.verification.api import router as verification_router

app = FastAPI()

app.include_router(verification_router, prefix="/api/v1", tags=["Verification"])

@app.get("/")
def read_root():
    """
    Root endpoint.
    :return: Welcome message
    """
    return {"message": "Welcome to the Access Verifier API"}
