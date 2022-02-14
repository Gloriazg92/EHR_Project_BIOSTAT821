import pytest
import HW03
import First_Age
from datetime import datetime
from HW03 import parse_data, num_older_than, sick_patients
from First_Age import age_first_adm


def test_parse_data():
    """
    Test function parse_data to check whether the function read the correct data from the dataset
    """
    assert HW03.data_patient["PatientGender"][0] == "Male"
    assert HW03.data_lab["LabUnits"][0] == "rbc/hpf"


def test_num_older_than():
    """
    Test function num_older_than to check whether the function returns the correct number of patients
    """
    assert HW03.num_older_than(51.2, HW03.data_patient) == 77


def test_sick_patients():
    """
    Test function sick_patients to check whether the length of sample output match the number of sets from the dataset 
    """
    assert len(HW03.sick_patients("METABOLIC: ALBUMIN", ">", 4.0, HW03.data_lab)) == 100


def test_age_first_adm():
    """
    Test function age_first_adm to chech whether it returns the age of a specific patient selected from the dataset
    """
    assert (
        First_Age.age_first_adm(
            HW03.data_patient, HW03.data_lab, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F"
        )
        == 20.79
    )

