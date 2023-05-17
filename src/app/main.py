from agora_token_builder import RtcTokenBuilder
from fastapi import FastAPI, HTTPException
from typing import Union

from src.app.models import TokenResponse
from src.app.settings import settings

ROLES = {'publisher': 1, 'subscriber': 2}

app = FastAPI()


@app.get('/rtc/{channel_name}/{role}/{token_type}/{user_id}', )
def create_token(channel_name: str, role: str, token_type: Union[int, str], user_id: int,
                 expiry: int = 86400) -> TokenResponse:
    """
    :param channel_name: This is the channel name
    :param role: This is the role, it is is either a publisher or a subscriber
    :param token_type: This is the token type. It is either a Uid or can be left as a string with value userAccout
    :param user_id: This is the user id, more steps can be taken to vaildate the user id in the database. Can be left as 0 if not needed
    :param expiry: The number of seconds the token would be active for. Defaults to 24 hours
    :return: Return a token response
    """

    # Now validate that the correct role was given
    if role not in ROLES.keys():
        raise HTTPException(status_code=403, detail='Please specify a valid role, it can be publisher or subscriber')

    # Validate that the correct token type was returned
    if type(token_type) == str:
        # Calculate the token wit user account
        token = RtcTokenBuilder.buildTokenWithAccount(settings.APP_ID, settings.PRIMARY_CERTIFICATE, channel_name,
                                                      token_type, ROLES[role],
                                                      expiry)
    elif type(token_type) == int:
        # Calculate the token with the user uid
        # Can be 0, if further verification is not needed
        token = RtcTokenBuilder.buildTokenWithUid(settings.APP_ID, settings.PRIMARY_CERTIFICATE, channel_name, user_id,
                                                  ROLES[role], expiry)
    else:
        # Very sure Fast Api type checking system would have checked this though
        raise HTTPException(status_code=403, detail='Please specify a valid tokenType')

    return TokenResponse(rtcToken=token)
