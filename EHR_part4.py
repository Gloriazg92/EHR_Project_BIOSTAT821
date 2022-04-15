from datetime import datetime
import sqlite3

con = sqlite3.connect("ehr.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS Patient ([PatientID] STRING PRIMARY KEY, [PatientGender] STRING, [PatientDateOfBirth] DATETIME, [PatientRace] STRING)"
)

cur.execute(
    "CREATE TABLE IF NOT EXISTS Labs ([PatientID] STRING PRIMARY KEY, [AdmissionID] INTEGER, [LabName] STRING, [LabValue] FLOAT, [LabDateTime] DATETIME)"
)

with open("PatientCorePopulatedTable.txt", "r", encoding="utf-8-sig") as files:
    for line in files.readlines()[1:]:
        data_patient = list(map(lambda x: "'%s'" % x, line.split("\t")))
        cur.execute("INSERT INTO Patient VALUES(%s)" % ",".join(data_patient))
con.commit()

with open("LabsCorePopulatedTable.txt", "r", encoding="utf-8-sig") as files:
    for line in files.readlines()[1:]:
        data_lab = list(map(lambda x: "'%s'" % x, line.split("\t")))
        cur.execute("INSERT INTO Labs VALUES(%s)" % ",".join(data_lab))
con.commit()


class Patient:
    def __init__(self, cursor, PatientID):
        self.cursor = cursor
        self.PatientID = PatientID

    @property
    def gender(self):
        cmd = f"SELECT PatientGender FROM Patient WHERE Patient.PatientID = '{self.PatientID}'"
        self.cursor.execute(cmd)
        return self.cursor.fetchone()[0]

    @property
    def dob(self):
        cmd = f"SELECT PatientDateOfBirth FROM Patient WHERE Patient.PatientID = '{self.PatientID}'"
        self.cursor.execute(cmd)
        return datetime.strptime(self.cursor.fetchone()[0], "%Y-%m-%d %H:%M:%S.%f")

    @property
    def race(self):
        cmd = f"SELECT PatientRace FROM Patient WHERE Patient.PatientID = '{self.PatientID}'"
        self.cursor.execute(cmd)
        return self.cursor.fetchone()[0]

    @property
    def age(self):
        return round(float((datetime.now() - self.dob).days) / 365, 2)


class Lab:
    def __init__(self, cursor, PatientID):
        self.cursor = cursor
        self.PatientID = PatientID

    @property
    def admissionid(self):
        cmd = f"SELECT AdmissionID FROM Labs WHERE Labs.PatientID = '{self.PatientID}'"
        self.cursor.execute(cmd)
        return [admissionid[0] for admissionid in self.cursor.fetchall()]

    @property
    def name(self):
        cmd = f"SELECT LabName FROM Labs WHERE Labs.PatientID = '{self.PatientID}'"
        self.cursor.execute(cmd)
        return [name[0] for name in self.cursor.fetchall()]

    @property
    def value(self):
        cmd = f"SELECT LabValue FROM Labs WHERE Labs.PatientID = '{self.PatientID}'"
        self.cursor.execute(cmd)
        return [value[0] for value in self.cursor.fetchall()]

    @property
    def datetime(self):
        cmd = f"SELECT LabDateTime FROM Labs WHERE Labs.PatientID = '{self.PatientID}'"
        self.cursor.execute(cmd)
        return [
            datetime.strptime(datetime[0], "%Y-%m-%d %H:%M:%S.%f ")
            for datetime in self.cursor.fetchall()
        ]


# Old patients
def num_older_than(age: float, data_patient: list[Patient]) -> int:
    counter = 0
    for patient in data_patient:
        if patient.age > age:
            counter += 1
    return counter
    # N*(1+1)+N*(1+1) -> O(N)


# Sick patients
def sick_patients(
    lab_name: str,
    gt_lt: str,
    value: float,
    data_patient: list[Patient],
    admission_id: int,
) -> set[str]:
    if gt_lt != "<" and gt_lt != ">":
        raise ValueError(f"{gt_lt} should be a > or <")
    id_lab = set()
    cmd = "SELECT LabValue FROM Labs WHERE AdmissionID = '{admission_id}' AND LabName = '{lab_name}'"
    for patient in data_patient:
        patient.cursor.execute(cmd)
        try:
            lab_value = [LabValue[0] for LabValue in patient.cursor.fetchall()]
        except:
            print("No lab value for the patient")
        if gt_lt == ">" and lab_value > value:
            id_lab.add(patient.admissionid)
        elif gt_lt == "<" and lab_value < value:
            id_lab.add(patient.admissionid)
    return id_lab
    # N*(1+1+1+1+1) -> O(N)

