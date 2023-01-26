from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel

#parameters for _Creating_a_Profile_
class _Creating_a_Profile_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# Allowing users to register and create a profile for their dogs 
def _Creating_a_Profile_run(params: _Creating_a_Profile_params):
    #TODO: add code
    return "hello world"