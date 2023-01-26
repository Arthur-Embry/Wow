from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import types

description = """
Wow API helps you do awesome stuff.

## Notes



### Benefits of API

- **Discover dogs near you**: Our API allows you to easily find dogs near your current location, making it easy for pet owners to find the perfect match for their furry friend. 

- **Filter matches**: Our API makes it easy to filter matches by size, age, breed, and other criteria, so you can find the right pup for you. 

- **Easy setup**: Our API makes it easy to set up and manage your profile, so you can start connecting with your pup-mates in no time. 

- **Tinder for dogs**: Our API allows pet owners to connect with other pet owners, creating a Tinder-style experience for finding the perfect pup.

## Pages

[tinder-swipe-cards](../tinder-swipe-cards/index.html)


# Restfull Endpoints
"""

app = FastAPI(
    title="Wow",
    description=description,
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#exposure template
#exposure template
def expose(endpoint,service):
    
    #import the service and define the function and parameters
    service_import=__import__("app.api."+service+'_services')### if "/code" in os.getcwd() else __import__("api."+service+'_services')
    print(service_import.__dict__['api'].__dict__[service+'_services'].__dict__[endpoint+'_run'])
    function_import=service_import.__dict__['api'].__dict__[service+'_services'].__dict__[endpoint+'_run']
    function_params=service_import.__dict__['api'].__dict__[service+'_services'].__dict__[endpoint+'_params']

    # Decorate it with your decorator and then pass it to FastAPI
    def template(item: function_params):
        #catch special case of default parameters changing from string to tuple
        for i in item:
            if type(i[1])==tuple:
                setattr(item, i[0].split("=")[0], i[1][0])

        return function_import(item)

        
    globals()[endpoint+"_global"] = types.FunctionType(template.__code__, {}, name=template.__name__, argdefs=template.__defaults__, closure=template.__closure__)
    globals()[endpoint+"_global"].__name__ = endpoint
    globals()[endpoint+"_global"].__annotations__ = {"item": function_params}
    app.post("/"+endpoint)(globals()[endpoint+"_global"])

def remap(path, new_path):
    path = "app/"+path if "/code" in os.getcwd() else path
    @app.get("/"+new_path, response_class=HTMLResponse)
    async def serve_page():
        with open(path) as f:
            lines = f.readlines()
        return ''.join(lines)



expose("_Creating_a_Profile","_Creating_a_Profile")
expose("_Matching","_Matching")
expose("_Messaging","_Messaging")
expose("_Filtering","_Filtering")
expose("_Social","_Social")
expose("_Location","_Location")
expose("_Analytics","_Analytics")


app.mount("/tinder-swipe-cards", StaticFiles(directory="app/public/tinder-swipe-cards/dist"), name="static")