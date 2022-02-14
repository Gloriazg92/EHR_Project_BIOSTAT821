from datetime import datetime


def age_first_adm(patient_data, lab_data, patientID):
    """
    obtain the age of patient at his first lab
    return -1 if the patientID doesn't exit in the data
    """
    date = datetime.now()
    for i in range(len(lab_data["PatientID"])):
        if lab_data["PatientID"][i] == patientID:
            date_of_lab = datetime.strptime(
                lab_data["LabDateTime"][i], "%Y-%m-%d %H:%M:%S.%f"
            )
            if date_of_lab < date:
                date = date_of_lab
    age = -1
    for i in range(len(patient_data["PatientID"])):
        if patient_data["PatientID"][i] == patientID:
            date_of_birth = datetime.strptime(
                patient_data["PatientDateOfBirth"][i], "%Y-%m-%d %H:%M:%S.%f"
            )
            age = round(float((date - date_of_birth).days) / 365, 2)
    return age


if __name__ == "__main__":
    data_patient = parse_data(
        "/Users/guzhengyi/Desktop/BIOSTAT 821/PatientCorePopulatedTable.txt"
    )
    data_lab = parse_data(
        "/Users/guzhengyi/Desktop/BIOSTAT 821/LabsCorePopulatedTable.txt"
    )
    print(age_first_lab(data_patient, data_lab, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F"))
