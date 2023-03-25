from fastapi import FastAPI

# now we will import object from config.py file into this file
from core.config import settings

from db.session import engine
from db.base_class import Base

#----------------------------------------------------------------------------------------------------------#

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title = settings.PROJECT_TITLE, version = settings.PROJECT_VERSION)
    create_tables()
    return app

# now we will use this "app" object to create different routes/endpoints/urls which our users will hit
app = start_application()


# creating a "GET" route
@app.get('/')
def hello_api():
    return {'details' : 'hello world'} 
