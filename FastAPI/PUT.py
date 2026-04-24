from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional
from fastapi.responses import JSONResponse
import json

app= FastAPI()

      
def load_data():
    with open('patients.json','r') as f:
        data= json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


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
            return 'Overweight'
        else:
            return 'Obese'


class Patient_Update(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=110)]
    gender: Annotated[Optional[Literal['male','female','others']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


@app.put('/edit/{patient_id}')

def update_patient(patient_id:str,patient_update:Patient_Update):
    data= load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail='patient_id is not present in data')

    existing_data= data[patient_id]

    updated_patient_info= patient_update.model_dump(exclude_unset=True) #model_dump is used to covert json data into dict. data and exclude_unset is uded to extract only those values from the pydantic whose value has been set by user....

    for key,value in updated_patient_info.items():
        existing_data[key]=value

    existing_data['id']= patient_id
    new_data=Patient(**existing_data)  #passing our updated data with previous pydantic schema to compute bmi and verdit field also....
    existing_data= new_data.model_dump(exclude='id')  #as id already mentioned in api_points so we are taking whole schema excluding id values....

    data[patient_id]= existing_data

    save_data(data)

    return JSONResponse(status_code=200,content={'message':'patient updated successfully'})


    