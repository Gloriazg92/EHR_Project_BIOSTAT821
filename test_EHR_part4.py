import pytest
import sqlite3
from EHR_part4 import Patient, Lab
from EHR_part4 import *

con = sqlite3.connect("ehr.db")
cur = con.cursor()

patient2 = Patient(
    gender="Male",
    dob=datetime.strptime("1947-12-28 02:45:40.547", "%Y-%m-%d %H:%M:%S.%f"),
    race="Unknown",
)
patient3 = Patient(
    gender="Male",
    dob=datetime.strptime("1952-01-18 19:51:12.91", "%Y-%m-%d %H:%M:%S.%f"),
    race="African American",
)
lab1 = Lab(
    admissionid="1",
    name="URINALYSIS: RED BLOOD CELLS",
    value="1.8",
    datetime=datetime.strptime("1952-01-18 19:51:12.91", "%Y-%m-%d %H:%M:%S.%f"),
)
lab2 = Lab(
    admissionid="1",
    name="URINALYSIS: RED BLOOD CELLS",
    value="1.8",
    datetime=datetime.strptime("1947-12-28 02:45:40.547", "%Y-%m-%d %H:%M:%S.%f"),
)
a = parse_patient_data("Patient_1.txt")


def test_class_patient():
    patient_test_1 = Patient(cur, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F")
    assert patient_test_1.gender == "Male"


def test_class_lab():
    lab_test_1 = Lab(cur, "1A8791E3-A61C-455A-8DEE-763EB90C9B2C")
    assert lab_test_1.units == "rbc/hpf"


def test_num_older_than():
    assert num_older_than(float(80), [patient2, patient3]) == 0
    assert num_older_than(float(20), [patient2, patient3]) == 2


def test_sick_patients():
    assert sick_patients("URINALYSIS: RED BLOOD CELLS", ">", 1, a, 1) == set(["1", "2"])
