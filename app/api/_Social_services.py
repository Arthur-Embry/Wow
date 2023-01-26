from fastapi.responses import StreamingResponse
from typing import Union
from pydantic import BaseModel

#parameters for _Social_
class _Social_params(BaseModel):
    #TODO: add parameters
    temp: Union[str,None]="",

# Allowing users to view other user profiles, like and comment on posts, and follow other dogs 
def _Social_run(params: _Social_params):
    #TODO: add code
    return "hello world"