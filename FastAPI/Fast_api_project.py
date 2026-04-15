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
    return sorted_data


#pydantic schema for data which we are inserting as per client request into server request....
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

@app.post('/create')
def create_patient(patient:Patient):

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


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    data= load_data()

    if patient_id not in  data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200,content={'message': f'Patient {patient_id} deleted'})




    



