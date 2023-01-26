from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel

#parameters for _Messaging_
class _Messaging_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# Allowing users to message and chat with potential matches 
def _Messaging_run(params: _Messaging_params):
    #TODO: add code
    return "hello world"