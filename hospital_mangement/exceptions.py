class HospitalManagementError(Exception):
    """Base exception for the Hospital Management System."""
    pass


class PatientNotFoundError(HospitalManagementError):
    """Raised when a patient is not found."""
    pass


class PatientAlreadyExistsError(HospitalManagementError):
    """Raised when a patient already exists."""
    pass


class InvalidPatientDataError(HospitalManagementError):
    """Raised when patient data is invalid."""
    pass