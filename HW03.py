from datetime import datetime

# Data parsing
def parse_data(filename):
    """ For EHR data, it is more efficient to use dictionary than only lists.
    Dictionay associates each key with values, so that we can easily look data up by key.
    List can only go element by element until the result is found.
    In this case, I chose to create a list for dic
    """
    f = open(filename, "r", encoding="utf-8-sig")
    data = {}
    lines = f.readlines()
    labels = lines[0].split()
    for label in labels:  # O(1)
        data[label] = []  # O(1)
    for line in lines[1:]:  # N-1 times
        line_p = line.strip().split("\t")  # O(1)
        for i in range(len(labels)):  # M times -- 7
            data[labels[i]].append(line_p[i])  # O(1)
    return data
    # 1+1+(N-1)*(1+M*1) -> O(N*M)


# Old patients
def num_older_than(age, data):
    data_patient["age"] = []
    count = 0
    for date in data_patient["PatientDateOfBirth"]:  # N times
        date_of_birth = datetime.strptime(date.split()[0], "%Y-%m-%d")  # O(1)
        data_patient["age"].append(
            float((datetime.now() - date_of_birth).days) / 365
        )  # O(1)
    for i in range(len(data_patient["age"])):  # N times
        if data_patient["age"][i] > age:  # O(1)
            count += 1  # O(1)
    return count
    # N*(1+1)+N*(1+1) -> O(N)


# Sick patients
def sick_patients(lab, gt_lt, value, data):
    id_lab = []
    for i in range(len(data_lab["LabName"])):  # N times
        if data_lab["LabName"][i] == lab:  # O(1)
            if gt_lt == ">" and float(data_lab["LabValue"][i]) > value:  # O(1)
                id_lab.append(data_lab["PatientID"][i])  # O(1)
            elif gt_lt == "<" and float(data_lab["LabValue"][i]) < value:  # O(1)
                id_lab.append(data_lab["PatientID"][i])  # O(1)
    return set(id_lab)
    # N*(1+1+1+1+1) -> O(N)


if __name__ == "__main__":
    data_patient = parse_data(
        "/Users/guzhengyi/Desktop/BIOSTAT 821/PatientCorePopulatedTable.txt"
    )
    data_lab = parse_data(
        "/Users/guzhengyi/Desktop/BIOSTAT 821/LabsCorePopulatedTable.txt"
    )

    print(num_older_than(51.2, data_patient))
    print(sick_patients("METABOLIC: ALBUMIN", ">", 4.0, data_lab))