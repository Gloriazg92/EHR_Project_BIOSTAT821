from class_EHR_analysis import *
import pytest


def test_build_data_patient():
    """Use small data files created: Patient_1 and Labs_1 """
    patient_test = build_data_patient("Patient_1.txt")
    assert patient_test[0].gender == "Male"


def test_build_data_lab():
    lab_test = build_data_lab("Labs_1.txt")
    assert lab_test[0].units == "rbc/hpf"
