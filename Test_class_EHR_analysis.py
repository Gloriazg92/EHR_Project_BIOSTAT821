from class_EHR_analysis import *
import pytest


def test_build_data_patient():
    patient_test = build_data_patient(
        "/Users/guzhengyi/Desktop/BIOSTAT 821/PatientCorePopulatedTable.txt"
    )
    assert patient_test[0].gender == "Male"


def test_build_data_lab():
    lab_test = build_data_lab(
        "/Users/guzhengyi/Desktop/BIOSTAT 821/LabsCorePopulatedTable.txt"
    )
    assert lab_test[0].units == "rbc/hpf"
