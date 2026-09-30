class HospitalManagementError(Exception):
    """Base exception for the Hospital Management System."""
    pass


class DuplicateRecordError(HospitalManagementError):
    """Raised when a duplicate record already exists."""
    pass


class RecordNotFoundError(HospitalManagementError):
    """Raised when a record is not found."""
    pass


class InvalidPatientDataError(HospitalManagementError):
    """Raised when patient data is invalid."""
    pass
