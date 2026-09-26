"""Configuration values and portable paths for Hospital_Management"""

from pathlib import Path

APPLICATION_NAME="HOSPITAL MANAGEMENT SYSTEM"
AAPLICATION_VERSION="v1.0"
COLLAGE_NAME="ABC Hospital"


ROOT_DIR=Path(__file__).resolve().parent

DATA_DIR=ROOT_DIR/"data"
PATIENTS_FILE=DATA_DIR/"patients.csv"

DATA_DIR.mkdir(parents=True, exist_ok=True)