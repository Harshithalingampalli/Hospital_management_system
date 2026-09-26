def ask(label, optional=False):
    """Read nonblank input unless the field is optional."""
    while True:
        value = input(f"{label}: ").strip()

        if value or optional:
            return value

        print(f"{label} cannot be blank.")


def display_patients(patients):
    if not patients:
        print("No patients found.")
        return

    print("\n" + "-" * 115)

    print(
        f"{'PATIENT ID':<14}"
        f"{'NAME':<18}"
        f"{'AGE':<6}"
        f"{'GENDER':<10}"
        f"{'CONTACT':<14}"
        f"{'ADDRESS':<25}"
        f"{'BLOOD GROUP':<14}"
        f"{'ACTIVE':<8}"
    )

    print("-" * 115)

    for patient in patients:
        print(
            f"{patient.patient_id:<14}"
            f"{patient.name:<18}"
            f"{patient.age:<6}"
            f"{patient.gender:<10}"
            f"{patient.contact:<14}"
            f"{patient.address:<25}"
            f"{patient.blood_group:<14}"
            f"{str(patient.active):<8}"
        )

    print("-" * 115)
```
