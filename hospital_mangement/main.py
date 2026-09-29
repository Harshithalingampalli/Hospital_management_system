from hospital_mangement.ui.menu import patient_menu
from hospital_mangement.services.patient_services import PatientService
from hospital_mangement.storage.csvStore import CSVStore
from config import PATIENT_FILE


PATIENT_FIELDS = [
    "patient_id",
    "name",
    "age",
    "gender",
    "contact",
    "address",
    "blood_group",
    "active"
]


def build_application():
    store = CSVStore(
        PATIENT_FILE,
        PATIENT_FIELDS,
        "patient_id"
    )

    patient_service = PatientService(store)

    return patient_service


if __name__ == "__main__":
    patient_service = build_application()
    patient_menu(patient_service)
