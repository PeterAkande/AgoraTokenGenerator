from pydantic import BaseModel


class TokenRequest(BaseModel):
    """
    This would form the structure of the body of the request
    """
    channel_name: str

    pass


class TokenResponse(BaseModel):
    """
    This would form the structure of the response of the request
    """
    rtcToken: str
