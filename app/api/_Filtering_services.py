from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel

#parameters for _Filtering_
class _Filtering_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# Allowing users to set preferences and filter potential matches 
def _Filtering_run(params: _Filtering_params):
    #TODO: add code
    return "hello world"