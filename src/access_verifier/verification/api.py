"""
Verification router
"""
from fastapi import APIRouter, Header, HTTPException
from .service import verify_access

router = APIRouter()


@router.post("/verification")
def check_access(x_forwarded_for: str = Header(None)):
    """
        Endpoint to verify access based on the X-Forwarded-For header IP address.

        :param x_forwarded_for: The IP address from the X-Forwarded-For header
        :return: A JSON response with the status of the verification
        :raises HTTPException: 400 error if the X-Forwarded-For header is missing
                               401 error if the IP address is not allowed
    """
    if x_forwarded_for is None:
        raise HTTPException(status_code=400, detail="X-Forwarded-For header missing")

        # Assuming verify_access now takes both token and ip as arguments
    is_verified = verify_access(x_forwarded_for)

    if is_verified:
        return {"status": "verified"}
    raise HTTPException(status_code=401, detail="Ip address is not allowed")
