from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse
import json

app= FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data= json.load(f)
    return data


#GET HTTP method for retrieving data

@app.get("/")
def help():
    return {'message':'Patient Maangement Using API'}

@app.get("/about")
def about():
    return {'message':'A fully functional API to manage your patient records....'}


@app.get('/view')
def view():
    data= load_data()
    return data

#building checkpoint with PATH parameter for accessing a specific data...
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str=Path(...,description='ID of the patient in the DB',example='P001')):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail='Patient not found')
    
#building checkpoint with query parameter....

@app.get('/sort')
def sort_patient(sort_by: str= Query(...,description='sort on the basis of height ,weight,bmi'),order_by:str=Query('asc',description='sort on the basis of asc and desc')):
    valid_fields=['height','bmi','weight']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Selected field not present in {valid_fields}')
    
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order selected')
    
    data=load_data()
    sort_order= True if order_by == 'desc' else False
    sorted_data= sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return 
    



