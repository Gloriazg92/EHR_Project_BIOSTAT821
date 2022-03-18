from datetime import datetime


class Patient:
    def __init__(self, list_data):
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
    def __init__(self, list_data):
        self.id = list_data[0]
        self.value = list_data[3]
        self.units = list_data[4]


def build_data_patient(file_name: str) -> list[list[str]]:
    data = []
    with open(file_name, "r", encoding="utf-8-sig") as files:
        for line in files.readlines()[1:]:
            data.append(Patient(line.split("\t")))
    return data


def build_data_lab(file_name: str) -> list[list[str]]:
    data = []
    with open(file_name, "r", encoding="utf-8-sig") as files:
        for line in files.readlines()[1:]:
            data.append(Lab(line.split("\t")))
    return data


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
