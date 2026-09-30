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
    active: bool = True

    def to_row(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": str(self.age),
            "gender": self.gender,
            "contact": self.contact,
            "address": self.address,
            "blood_group": self.blood_group,
            "active": str(self.active)
        }

    @classmethod
    def from_row(cls, row):
        return cls(
            patient_id=row["patient_id"],
            name=row["name"],
            age=int(row["age"]),
            gender=row["gender"],
            contact=row["contact"],
            address=row["address"],
            blood_group=row["blood_group"],
            active=row["active"].lower() == "true"
        )
