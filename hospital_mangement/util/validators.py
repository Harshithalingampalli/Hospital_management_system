import re

from hospital_management.exceptions import ValidationError


def required_text(value, field_name):
    value = str(value).strip()

    if not value:
        raise ValidationError(f"{field_name} cannot be blank.")

    return value


def validate_patient_id(value):
    return required_text(value, "Patient ID")


def validate_name(value):
    value = required_text(value, "Name")

    if not all(char.isalpha() or char.isspace() for char in value):
        raise ValidationError("Name must contain only letters and spaces.")

    return value


def validate_age(value):
    try:
        value = int(value)
    except (TypeError, ValueError) as error:
        raise ValidationError("Age must be a whole number.") from error

    if value < 1 or value > 120:
        raise ValidationError("Age must be between 1 and 120.")

    return value


def validate_gender(value):
    value = required_text(value, "Gender").lower()

    if value not in ["male", "female", "other"]:
        raise ValidationError("Gender must be Male, Female, or Other.")

    return value


def validate_contact(value):
    value = required_text(value, "Contact number")

    if not value.isdigit() or len(value) != 10:
        raise ValidationError(
            "Contact number must contain exactly 10 digits."
        )

    return value


def validate_address(value):
    return required_text(value, "Address")


def validate_blood_group(value):
    value = required_text(value, "Blood group").upper()

    valid_groups = [
        "A+", "A-",
        "B+", "B-",
        "AB+", "AB-",
        "O+", "O-"
    ]

    if value not in valid_groups:
        raise ValidationError("Enter a valid blood group.")

    return value
