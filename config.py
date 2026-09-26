"""Configuration values and portable paths for Hospital Management System."""

from pathlib import Path

APPLICATION_NAME = "Hospital Management System"
APPLICATION_VERSION = "v1.0"
HOSPITAL_NAME = "SVEC Hospital"

ROOT_DIR = Path(__file__).resolve().parent

DATA_DIR = ROOT_DIR / "data"

PATIENT_FILE = DATA_DIR / "patients.csv"

DATA_DIR.mkdir(parents=True, exist_ok=True)