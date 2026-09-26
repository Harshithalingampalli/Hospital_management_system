from dataclasses import dataclass


@dataclass
class Patient:
  patient_id: str 
  name: str
  age: int
  gender: str
  contact: str
  address: str
  blood_group: str
  active:bool=True
  
  
  
  
  
