from fastapi import FastAPI

# now we will import object from config.py file into this file
from core.config import settings

#----------------------------------------------------------------------------------------------------------#

app = FastAPI(title = settings.PROJECT_TITLE, version = settings.PROJECT_VERSION)

# now we will use this "app" object to create different routes/endpoints/urls which our users will hit

# creating a "GET" route
@app.get('/')
def hello_api():
    return {'details' : 'hello world'} 
