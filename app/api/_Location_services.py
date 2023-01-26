from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel

#parameters for _Location_
class _Location_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# Allowing users to set their location and find nearby matches 
def _Location_run(params: _Location_params):
    #TODO: add code
    return "hello world"