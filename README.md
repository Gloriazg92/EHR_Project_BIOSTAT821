# EHR Project

## For end users:

Two EHR data files are provided:
"PatientCorePopulatedTable.txt" with patients' information. 
"LabsCorePopulatedTable.txt" with laboratory outcomes.
Input data files are all in the format of txt files. 

Download files "Hw03.py" and "First_Age.py", four functions can be imported.

**parse_data**
This function will read and parse the data files into dictionaries which has only one input 'filename'.

Example:
```python
>> data_patient = parse_data("PatientCorePopulatedTable.txt")
>> data_lab = parse_data("LabsCorePopulatedTable.txt")
```

**num_older_than**
This function will calculate the number of patients whose ages are larger than a specific number which have two inputs 'age' and 'data'. 
The input 'age' is an integer.
The input 'data' is a dictionary with compulsory key 'PatientDateOfBirth'.

Example:
```python
>> num_older_than(51.2, data_patient)
77
```

**sick_patients**
This function will return a (unique) set of patients who have a given test with value above (">") or below ("<") a given level in a specific lab. There are four inputs 'lab', 'gt_lt', 'value', 'data'.
The input 'lab' is the lab name.
The input 'gt_lt' is either '>' or '<'.
The input 'value' is the value to compare.
The input 'data' is a dictionary with compulsory keys 'PatientID', 'LabName'.

Example:
```python
>> sick_patients("METABOLIC: ALBUMIN", ">", 4.0, data_lab)
```

**age_first_adm**
This function will return the age of patient at first admission which have three inputs 'patient_data', 'lab_data' and 'patientID'
The input 'patient_data' is a dictionary with compulsory keys 'PatientID', 'PatientDateOfBirth'.
The input 'lab_data' is a dictionary with compulsory keys 'PatientID', 'LabDateTime'.
The input 'patientID' is a string.

Example:
```python
>> age_first_lab(data_patient, data_lab, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F")
20.79
```


## For contributors:
The test file "HW_4.py" which can be used to test all four functions by 'pytest'. Data should be in the required format from 'PatientCorePopulatedTable.txt' and 'LabsCorePopulatedTable.txt'. "HW_4.py", "HW03.py" and "Age_First.py" should be in the same folder in order for the testing. All four tests should pass, any changes of sample output can result in a failed test. 
