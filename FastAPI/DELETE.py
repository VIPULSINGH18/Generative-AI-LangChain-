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


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    data= load_data()

    if patient_id not in  data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200,content={'message': 'Patient deleted'})
