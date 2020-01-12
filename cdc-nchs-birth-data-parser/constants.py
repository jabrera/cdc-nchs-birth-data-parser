UNKNOWN_NOT_STATED = 'Unknown or not stated'

MONTH = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
    '99': UNKNOWN_NOT_STATED,
}

# RACE
RACE31 = {
    '01': 'White (only) [only one race reported] ',
    '02': 'Black (only)',
    '03': 'AIAN (American Indian or Alaskan Native) (only)',
    '04': 'Asian (only)',
    '05': 'NHOPI (Native Hawaiian or Other Pacific Islander) (only)',
    '06': 'Black and White',
    '07': 'Black and AIAN',
    '08': 'Black and Asian',
    '09': 'Black and NHOPI',
    '10': 'AIAN and White',
    '11': 'AIAN and Asian',
    '12': 'AIAN and NHOPI',
    '13': 'Asian and White',
    '14': 'Asian and NHOPI',
    '15': 'NHOPI and White',
    '16': 'Black, AIAN, and White',
    '17': 'Black, AIAN, and Asian',
    '18': 'Black, AIAN, and NHOPI',
    '19': 'Black, Asian, and White',
    '20': 'Black, Asian, and NHOPI',
    '21': 'Black, NHOPI, and White',
    '22': 'AIAN, Asian, and White',
    '23': 'AIAN, NHOPI, and White',
    '24': 'AIAN, Asian, and NHOPI',
    '25': 'Asian, NHOPI, and White',
    '26': 'Black, AIAN, Asian, and White',
    '27': 'Black, AIAN, Asian, and NHOPI',
    '28': 'Black, AIAN, NHOPI, and White',
    '29': 'Black, Asian, NHOPI, and White ',
    '30': 'AIAN, Asian, NHOPI, and White',
    '31': 'Black, AIAN, Asian, NHOPI, and White ',
}
RACE6 = {
    '1': 'White (only)',
    '2': 'Black (only)',
    '3': 'AIAN (only)',
    '4': 'Asian (only)',
    '5': 'NHOPI (only)',
    '6': 'More than one race',
}
RACE15 = {
    '01': 'White (only)',
    '02': 'Black (only)',
    '03': 'AIAN (only)',
    '04': 'Asian Indian (only)',
    '05': 'Chinese (only)',
    '06': 'Filipino (only)',
    '07': 'Japanese (only)',
    '08': 'Korean (only)',
    '09': 'Vietnamese (only)',
    '10': 'Other Asian (only)',
    '11': 'Hawaiian (only)',
    '12': 'Guamanian (only)',
    '13': 'Samoan (only)',
    '14': 'Other Pacific Islander (only)',
    '15': 'More than one race ',
}
BRACE = {
    '0': 'Other (not classified as White or Black)',
    '1': 'White',
    '2': 'Black',
    '3': 'American Indian or Alaskan Native',
    '4': 'Asian or Pacific Islander',
}
BRACE2 = {
    '1': 'White',
    '2': 'Black',
    '3': 'American Indian or Alaskan Native',
    '4': 'Asian or Pacific Islander',
    '9': UNKNOWN_NOT_STATED,
}
RACE_HISP = {
    '1': 'Non-Hispanic White (only)',
    '2': 'Non-Hispanic Black (only)',
    '3': 'Non-Hispanic AIAN (only)',
    '4': 'Non-Hispanic Asian (only)',
    '5': 'Non-Hispanic NHOPI (only)',
    '6': 'Non-Hispanic more than one race',
    '7': 'Hispanic',
    '8': 'Origin unknown or not stated',
    '9': 'Race unknown or not stated (Non-Hispanic) '
}

# HISPANIC
HISP_R = {
    '0': 'Non-Hispanic',
    '1': 'Mexican',
    '2': 'Puerto Rican',
    '3': 'Cuban',
    '4': 'Central and South American',
    '5': 'Other and Unknown Hispanic origin',
    '9': 'Hispanic origin not stated',
}

# AGE
AGE = {
    '12': '10 – 12 years',
    '13': '13 years',
    '14': '14 years',
    '15': '15 years',
    '16': '16 years',
    '17': '17 years',
    '18': '18 years',
    '19': '19 years',
    '20': '20 years',
    '21': '21 years',
    '22': '22 years',
    '23': '23 years',
    '24': '24 years',
    '25': '25 years',
    '26': '26 years',
    '27': '27 years',
    '28': '28 years',
    '29': '29 years',
    '30': '30 years',
    '31': '31 years',
    '32': '32 years',
    '33': '33 years',
    '34': '34 years',
    '35': '35 years',
    '36': '36 years',
    '37': '37 years',
    '38': '38 years',
    '39': '39 years',
    '40': '40 years',
    '41': '41 years',
    '42': '42 years',
    '43': '43 years',
    '44': '44 years',
    '45': '45 years',
    '46': '46 years',
    '47': '47 years',
    '48': '48 years',
    '49': '49 years',
    '50': '50 years and over',
}
AGE9 = {
    '1': 'Under 15 years',
    '2': '15-19 years',
    '3': '20-24 years',
    '4': '25-29 years',
    '5': '30-34 years',
    '6': '35-39 years',
    '7': '40-44 years',
    '8': '45-49 years',
    '9': '50-54 years',
}
AGE11 = {
    '01': 'Under 15 years',
    '02': '15-19 years',
    '03': '20-24 years',
    '04': '25-29 years',
    '05': '30-34 years',
    '06': '35-39 years',
    '07': '40-44 years',
    '08': '45-49 years',
    '09': '50-54 years',
    '10': '55-98 years',
    '11': 'Not stated',
}
AGE14 = {
    '01': 'Under 15 Years',
    '03': '15 years',
    '04': '16 years',
    '05': '17 years',
    '06': '18 years',
    '07': '19 years',
    '08': '20-24 years',
    '09': '25-29 years',
    '10': '30-34 years',
    '11': '35-39 years',
    '12': '40-44 years',
    '13': '45-49 years',
    '14': '50-54 years',
}


# EDUCATION
EDUC = {
    '1': '8th grade or less',
    '2': '9th through 12th grade with no diploma',
    '3': 'High school graduate or GED completed',
    '4': 'Some college credit, but not a degree.',
    '5': 'Associate degree (AA,AS)',
    '6': 'Bachelor’s degree (BA, AB, BS)',
    '7': 'Master’s degree (MA, MS, MEng, MEd, MSW, MBA)',
    '8': 'Doctorate (PhD, EdD) or Professional Degree (MD, DDS, DVM, LLB, JD)',
    '9': 'Unknown',
}

# REPORTING
REPORTING = {
    '0': 'Non-Reporting',
    '1': 'Reporting',
}

# CIG
CIG = {
    '00-97': '[value] cigarettes daily',
    '98': '98 or more cigarettes daily',
    '99': UNKNOWN_NOT_STATED,
}
CIG_R = {
    '0': 'Nonsmoker',
    '1': '1-5',
    '2': '6-10',
    '3': '11-20',
    '4': '21-40',
    '5': '41 or more',
    '6': UNKNOWN_NOT_STATED,
}

# OTHERS
YNUX = {
    'Y': 'Yes',
    'N': 'No',
    'U': 'Unknown',
    'X': 'Not Applicable',
}
YNU = {
    'Y': 'Yes',
    'N': 'No',
    'U': UNKNOWN_NOT_STATED,
}
TRUE_FALSE_NOT_REPORTED = {
    '1': 'True',
    '0': 'False',
    '9': 'Not Reported',
}