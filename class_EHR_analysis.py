from datetime import datetime


class Patient:
    def __init__(self, list_data: list[str]) -> None:
        """Initial function"""
        self.id = list_data[0]
        self.gender = list_data[1]
        self.dob = datetime.strptime(list_data[2], "%Y-%m-%d %H:%M:%S.%f")
        self.race = list_data[3]

    @property
    def age(self):
        """A property age"""
        return round(float((datetime.now() - self.dob).days) / 365, 2)


class Lab:
    def __init__(self, list_data: list[str]) -> None:
        self.id = list_data[0]
        self.admissionid = list_data[1]
        self.name = list_data[2]
        self.value = list_data[3]
        self.units = list_data[4]
        self.datetime = datetime.strptime(list_data[5], "%Y-%m-%d %H:%M:%S.%f ")


def build_data_patient(file_name: str) -> list[Patient]:
    data_patient = []
    with open(file_name, "r", encoding="utf-8-sig") as files:
        for line in files.readlines()[1:]:
            data_patient.append(Patient(line.split("\t")))
    return data_patient


def build_data_lab(file_name: str) -> list[Lab]:
    data_lab = []
    with open(file_name, "r", encoding="utf-8-sig") as files:
        for line in files.readlines()[1:]:
            data_lab.append(Lab(line.split("\t")))
    return data_lab


def num_older_than(age: float, data_patient: list[Patient]) -> int:
    counter = 0
    for patient in data_patient:
        if patient.age > age:
            counter += 1
    return counter


def sick_patients(
    lab_name: str, gt_lt: str, value: float, data_lab: list[Lab]
) -> set[str]:
    if gt_lt != "<" and gt_lt != ">":
        raise ValueError(f"{gt_lt} should be a > or <")
    id_lab = set()
    for lab in data_lab:
        if lab.name == lab_name:
            if gt_lt == ">" and lab.value > value:
                id_lab.add(lab.id)
            elif gt_lt == "<" and lab.value < value:
                id_lab.add(lab.id)
    return id_lab


def age_first_adm(
    data_patient: list[Patient], data_lab: list[Lab], patientID: str
) -> float:
    date_list = []
    for lab in data_lab:
        if lab.admissionid == "1" and lab.id == patientID:
            date_list.append(lab.datetime)
    date_of_lab = data_lab[0].datetime
    for date in date_list:
        if date_of_lab < date:
            date = date_of_lab
    for patient in data_patient:
        if patient.id == patientID:
            age = round(float((date - patient.dob).days) / 365, 2)
            return age


if __name__ == "__main__":
    print(
        build_data_patient(
            "/Users/guzhengyi/Desktop/BIOSTAT 821/PatientCorePopulatedTable.txt"
        )[0].gender
    )
    print(
        build_data_lab(
            "/Users/guzhengyi/Desktop/BIOSTAT 821/LabsCorePopulatedTable.txt"
        )[0].units
    )
