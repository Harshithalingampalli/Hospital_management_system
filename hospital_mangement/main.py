from hospital_management.ui.menus import patient_menu
from hospital_management.services.patient_services import PatientService
from hospital_management.storage.csv_store import CSVStore
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
