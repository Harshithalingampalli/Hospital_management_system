from hospital_mangement.exceptions import DuplicateRecordError, RecordNotFoundError
from hospital_mangement.models import Patient


class PatientService:
    """Business operations and rules for Patient Records."""

    def __init__(self, store):
        self.store = store

    def add_patient(self, patient):
        if self.store.find(patient.patient_id):
            raise DuplicateRecordError("Patient ID already exists.")

        self.store.add(patient.to_row())
        return patient

    def get_patient(self, patient_id):
        row = self.store.find(patient_id.strip().upper())

        if not row:
            raise RecordNotFoundError("Patient was not found.")

        return Patient.from_row(row)

    def list_patients(self, active_only=False):
        patients = [
            Patient.from_row(row)
            for row in self.store.get_all()
        ]

        if active_only:
            patients = [
                patient for patient in patients
                if patient.active
            ]

        return sorted(
            patients,
            key=lambda patient: patient.patient_id
        )

    def search_patients(self, search_text):
        search_text = search_text.strip().lower()

        return [
            patient
            for patient in self.list_patients()
            if search_text in patient.patient_id.lower()
            or search_text in patient.name.lower()
            or search_text in patient.contact.lower()
        ]

    def update_patient(self, patient_id, **changes):
        patient = self.get_patient(patient_id)

        for field_name, value in changes.items():
            if value not in (None, "") and hasattr(patient, field_name):
                setattr(patient, field_name, value)

        self.store.update(patient.to_row())

        return patient

    def deactivate_patient(self, patient_id):
        patient = self.get_patient(patient_id)

        patient.active = False

        self.store.update(patient.to_row())

        return patient

    def activate_patient(self, patient_id):
        patient = self.get_patient(patient_id)

        patient.active = True

        self.store.update(patient.to_row())

        return patient
