from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse
import json

app= FastAPI()

class Patient(BaseModel):
    id: Annotated[str,Field(...,description='ID of the patient',exaples=['P001'])]
    name:Annotated[str,Field(...,description='Nmae of the patient')]
    city:Annotated[str,Field(...,description='City where patient is living')]
    age:Annotated[int,Field(...,gt=0,lt=110,description='Age of the patient')]
    gender:Annotated[Literal['male','female','others'],Field(...,description='gender of the patient')]
    height: Annotated[float,Field(...,gt=0,description='height of the patient')]
    weight:Annotated[float,Field(...,gt=0,description='weight of the patient')]

    @computed_field
    @property
    def bmi(self)->float:
        bmi= round((self.weight/self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return 'Underweight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi<30:
            return 'Obese'
        else:
            return 'Overweight'
        
def load_data():
    with open('patients.json','r') as f:
        data= json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.post('/create')
def create(patient:Patient):

    #loading existing data
    data=load_data()

    #check if already data is present or not
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Paitient data already present')

    #adding new patient data
    data[patient.id]=patient.model_dump(exclude=['id'])

    #saving our added data into our main data
    save_data(data)

    return JSONResponse(status_code=201,content={'message':'Patient data is loaded successfully'})






