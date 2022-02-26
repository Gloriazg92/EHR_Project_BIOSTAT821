from HW03 import parse_data, num_older_than, sick_patients, age_first_adm


def test_parse_data():
    """
    Test function parse_data to check whether the function read the correct data from the dataset
    """
    """Use parse_data for small data files created: Patient_1 and Labs_1 """
    patients = parse_data("/Users/guzhengyi/Desktop/BIOSTAT 821/Patient_1.txt")
    labs = parse_data("/Users/guzhengyi/Desktop/BIOSTAT 821/Labs_1.txt")
    assert patients["PatientGender"][0] == "Male"
    assert labs["LabUnits"][0] == "rbc/hpf"


def test_num_older_than():
    """
    Test function num_older_than to check whether the function returns the correct number of patients
    """
    patients_sample = {
        "PatientDateOfBirth": [
            datetime.strptime("2010-07-01 10:10:10.000", "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime("1940-07-01 10:10:10.000", "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime("1960-07-01 10:10:10.000", "%Y-%m-%d %H:%M:%S.%f"),
        ]
    }
    assert num_older_than(55, patients_sample) == 2


def test_sick_patients():
    """
    Test function sick_patients to check whether the length of sample output match the number of sets from the dataset 
    """
    labs_sample = {
        "LabName": ["lab1", "lab2", "lab2"],
        "PatientID": ["a", "b", "c"],
        "LabValue": [2, 4.2, 9],
    }
    assert sick_patients("lab2", ">", 5.0, labs_sample) == ["c"]


def test_age_first_adm():
    """
    Test function age_first_adm to chech whether it returns the age of a specific patient selected from the dataset
    """
    patients_sample = {
        "PatientID": ["a", "b", "c"],
        "PatientDateOfBirth": [
            datetime.strptime("2010-07-01 10:10:10.000", "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime("1940-07-01 10:10:10.000", "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime("1960-07-01 10:10:10.000", "%Y-%m-%d %H:%M:%S.%f"),
        ],
    }
    labs_sample = {
        "PatientID": ["c", "b", "c"],
        "LabDateTime": [
            datetime.strptime("1990-08-01 10:10:10.000", "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime("1970-07-01 10:10:10.000", "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime("1992-08-01 10:10:10.000", "%Y-%m-%d %H:%M:%S.%f"),
        ],
    }
    assert age_first_adm(patients_sample, labs_sample, "c") == 30.00

