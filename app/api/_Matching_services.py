from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel

#parameters for _Matching_
class _Matching_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# Generating matches between user's dogs and other potential matches 
def _Matching_run(params: _Matching_params):
    #TODO: add code
    return "hello world"