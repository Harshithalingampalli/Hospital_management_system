def patient_menu(patient_service):
    while True:
        print("\n==============================")
        print("   HOSPITAL MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. Display All Patients")
        print("4. Update Patient")
        print("5. Deactivate Patient")
        print("6. Activate Patient")
        print("7. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_patient_menu(patient_service)

        elif choice == "2":
            search_patient_menu(patient_service)

        elif choice == "3":
            display_patients_menu(patient_service)

        elif choice == "4":
            update_patient_menu(patient_service)

        elif choice == "5":
            deactivate_patient_menu(patient_service)

        elif choice == "6":
            activate_patient_menu(patient_service)

        elif choice == "7":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


def add_patient_menu(patient_service):
    print("\n--- Add Patient ---")

    patient_id = input("Patient ID: ")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    contact = input("Contact: ")
    address = input("Address: ")
    blood_group = input("Blood Group: ")

    from hospital_mangement.models import Patient
    try:
        patient = Patient(
            patient_id=patient_id,
            name=name,
            age=int(age),
            gender=gender,
            contact=contact,
            address=address,
            blood_group=blood_group
        )

        patient_service.add_patient(patient)

        print("Patient added successfully.")

    except Exception as e:
        print(f"Error: {e}")


def search_patient_menu(patient_service):
    print("\n--- Search Patient ---")

    search_text = input("Enter Patient ID, Name or Contact: ")

    patients = patient_service.search_patients(search_text)

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print_patient(patient)


def display_patients_menu(patient_service):
    print("\n--- All Patients ---")

    patients = patient_service.list_patients()

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print_patient(patient)


def update_patient_menu(patient_service):
    print("\n--- Update Patient ---")

    patient_id = input("Enter Patient ID: ")

    try:
        patient = patient_service.get_patient(patient_id)

        print("Press Enter to keep the existing value.")

        name = input(f"Name [{patient.name}]: ")
        age = input(f"Age [{patient.age}]: ")
        gender = input(f"Gender [{patient.gender}]: ")
        contact = input(f"Contact [{patient.contact}]: ")
        address = input(f"Address [{patient.address}]: ")
        blood_group = input(f"Blood Group [{patient.blood_group}]: ")

        changes = {
            "name": name,
            "age": int(age) if age else None,
            "gender": gender,
            "contact": contact,
            "address": address,
            "blood_group": blood_group
        }

        patient_service.update_patient(patient_id, **changes)

        print("Patient updated successfully.")

    except Exception as e:
        print(f"Error: {e}")


def deactivate_patient_menu(patient_service):
    print("\n--- Deactivate Patient ---")

    patient_id = input("Enter Patient ID: ")

    try:
        patient_service.deactivate_patient(patient_id)
        print("Patient deactivated successfully.")

    except Exception as e:
        print(f"Error: {e}")


def activate_patient_menu(patient_service):
    print("\n--- Activate Patient ---")

    patient_id = input("Enter Patient ID: ")

    try:
        patient_service.activate_patient(patient_id)
        print("Patient activated successfully.")

    except Exception as e:
        print(f"Error: {e}")


def print_patient(patient):
    print("\n------------------------------")
    print(f"Patient ID   : {patient.patient_id}")
    print(f"Name         : {patient.name}")
    print(f"Age          : {patient.age}")
    print(f"Gender       : {patient.gender}")
    print(f"Contact      : {patient.contact}")
    print(f"Address      : {patient.address}")
    print(f"Blood Group  : {patient.blood_group}")
    print(f"Active       : {patient.active}")
    print("------------------------------")
