import string
from typing import Union
from fastapi import FastAPI
from classes.lawmaker.lawmaker import Lawmaker
from classes.review.review import Review
from classes.app.andoidapp import AndroidApp
from pydantic import BaseModel


app = FastAPI()
lawmaker = Lawmaker()
review = Review()
android_app = AndroidApp()

###################################################LAWMAKER###################################################
#GET
@app.get("/lawmaker")
def read_root():     
     return lawmaker.index()
@app.get("/lawmaker/view")
def get_view():     
     return lawmaker.view()     

@app.get("/lawmaker/view/{law_id}")
def get_view(law_id: int):     
     return lawmaker.show(law_id)     

@app.get("/lawmaker/search/{law_string}")
def get_search(law_string: str):     
     return lawmaker.search(law_string)     




###################################################REVIEW###################################################
#GET
@app.get("/review")
def read_root():     
     return review.index()

###################################################ANDROID APP###################################################
#GET
@app.get("/app")
def read_root():     
     return android_app.index()

#testing 1