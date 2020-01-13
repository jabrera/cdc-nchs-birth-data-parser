import constants

columns = {
    '2016': {
        'DOB_YY': {
            'start': 9,
            'end': 12,
            'value': None,
            'definition': None
        },
        'DOB_MM': {
            'start': 13,
            'end': 14,
            'value': None,
            'definition': None,
            'valueDefinition': constants.MONTH
        },
        'DOB_TT': {
            'start': 19,
            'end': 22,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '9999': 'Not Stated',
            }
        },
        'DOB_WK': {
            'start': 23,
            'end': 23,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Sunday',
                '2': 'Monday',
                '3': 'Tuesday',
                '4': 'Wednesday',
                '5': 'Thursday',
                '6': 'Friday',
                '7': 'Saturday',
            }
        },
        'BFACIL': {
            'start': 32,
            'end': 32,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Hospital',
                '2': 'Freestanding Birth Center',
                '3': 'Home (intended)',
                '4': 'Home (not intended)',
                '5': 'Home (unknown if intended)',
                '6': 'Clinic / Doctor\'s Office',
                '7': 'Other',
                '9': 'Unknown',
            }
        },
        'F_FACILITY': {
            'start': 33,
            'end': 33,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'BFACIL3': {
            'start': 50,
            'end': 50,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'In Hospital',
                '2': 'Not in Hospital',
                '3': constants.UNKNOWN_NOT_STATED,
            }
        },
        'MAGE_IMPFLG': {
            'start': 73,
            'end': 73,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Age not imputed',
                '1': 'Age imputed',
            }
        },
        'MAGE_REPFLG': {
            'start': 74,
            'end': 74,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Reported age not used',
                '1': 'Reported age used',
            }
        },
        'MAGER': {
            'start': 75,
            'end': 76,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE
        },
        'MAGER14': {
            'start': 77,
            'end': 78,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE14
        },
        'MAGER9': {
            'start': 79,
            'end': 79,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE9
        },
        'MBSTATE_REC': {
            'start': 84,
            'end': 84,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Born in the U.S. (50 US States)',
                '2': 'Born outside the U.S. (includes possessions)',
                '3': constants.UNKNOWN_NOT_STATED,
            }
        },
        'RESTATUS': {
            'start': 104,
            'end': 104,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '__MBSTATE_REC': {
                    '1': {
                        '1': 'RESIDENT: State and county of occurrence and residence are the same.',
                        '2': 'INTRASTATE NONRESIDENT: State of occurrence and residence are the same but county is different.',
                        '3': 'INTERSTATE NONRESIDENT: State of occurrence and residence are different but both are one of the 50 US states or District of Columbia.',
                        '4': 'FOREIGN RESIDENT: The state of residence is not one of the 50 US states or District of Columbia.',
                    },
                    '2': {
                        '1': 'RESIDENT: State and county of occurrence and residence  residence are the same. (Unique to Guam, all US residents are considered residents of Guam and thus are assigned 1.)',
                        '2': 'INTRATERRITORY NONRESIDENT: Territory of occurrence and residence are the same but county is different.',
                        '3': 'INTERTERRITORY RESIDENT: Territory of occurrence and residence are different but both are US Territories.',
                        '4': 'FOREIGN RESIDENT: The residence is not a US Territory.',
                    }
                }
            }
        },
        'MRACE31': {
            'start': 105,
            'end': 106,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE31
        },
        'MRACE6': {
            'start': 107,
            'end': 107,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE6
        },
        'MRACE15': {
            'start': 108,
            'end': 109,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE15
        },
        'MBRACE': {
            'start': 110,
            'end': 110,
            'value': None,
            'definition': None,
            'valueDefinition': constants.BRACE
        },
        'MRACEIMP': {
            'start': 111,
            'end': 111,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Mother\'s race not imputed',
                '1': 'Unknown race imputed',
                '2': 'All other races, formerly coded 09, imputed.',
            }
        },
        'MHISP_R': {
            'start': 115,
            'end': 115,
            'value': None,
            'definition': None,
            'valueDefinition': constants.HISP_R
        },
        'F_MHISP': {
            'start': 116,
            'end': 116,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'MRACEHISP': {
            'start': 117,
            'end': 117,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE_HISP
        },
        'MAR_P': {
            'start': 119,
            'end': 119,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'DMAR': { #X
            'start': 120,
            'end': 120,
            'value': None,
            'definition': None,
            # 'valueDefinition': {
            # }
        },
        'MAR_IMP': {
            'start': 121,
            'end': 121,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Marital Status not imputed',
                '1': 'Marital Status imputed',
            }
        },
        'F_MAR_P': {
            'start': 123,
            'end': 123,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'MEDUC': {
            'start': 124,
            'end': 124,
            'value': None,
            'definition': None,
            'valueDefinition': constants.EDUC
        },
        'F_MEDUC': {
            'start': 126,
            'end': 126,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'FAGERPT_FLG': {
            'start': 142,
            'end': 142,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Father\'s reported age not used',
                '1': 'Father\'s reported age used',
            }
        },
        'FAGECOMB': {
            'start': 147,
            'end': 148,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'FAGEREC11': {
            'start': 149,
            'end': 150,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE11
        },
        'FRACE31': {
            'start': 151,
            'end': 152,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE31
        },
        'FRACE6': {
            'start': 153,
            'end': 153,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE6
        },
        'FRACE15': {
            'start': 154,
            'end': 155,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE15
        },
        'FBRACE': {
            'start': 156,
            'end': 156,
            'value': None,
            'definition': None,
            'valueDefinition': constants.BRACE2
        },
        'FHISP_R': {
            'start': 160,
            'end': 160,
            'value': None,
            'definition': None,
            'valueDefinition': constants.HISP_R
        },
        'F_FHISP': {
            'start': 161,
            'end': 161,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'FRACEHISP': {
            'start': 162,
            'end': 162,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE_HISP
        },
        'FEDUC': {
            'start': 163,
            'end': 163,
            'value': None,
            'definition': None,
            'valueDefinition': constants.EDUC
        },
        'F_FEDUC': {
            'start': 165,
            'end': 165,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'PRIORLIVE': {
            'start': 171,
            'end': 172,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'PRIORDEAD': {
            'start': 173,
            'end': 174,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'PRIORTERM': {
            'start': 175,
            'end': 176,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'LBO_REC': {
            'start': 179,
            'end': 179,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '8': '8 or more live births',
                '9': constants.UNKNOWN_NOT_STATED,
            }
        },
        'TBO_REC': {
            'start': 182,
            'end': 182,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '8': '8 or more live births',
                '9': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILLB_R': {
            'start': 198,
            'end': 200,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '888': 'Not applicable / 1st live birth',
                '999': '999 Unknown or not stated',
            }
        },
        'ILLB_R11': {
            'start': 201,
            'end': 202,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'Zero to 3 months (plural delivery)',
                '01': '4 to 11 months',
                '02': '12 to 17 months',
                '03': '18 to 23 months',
                '04': '24 to 35 months',
                '05': '36 to 47 months',
                '06': '48 to 59 months',
                '07': '60 to 71 months',
                '08': '72 months and over',
                '88': 'Not applicable (1st live birth)',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILOP_R': {
            'start': 206,
            'end': 208,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '888': 'Not applicable / 1st live birth',
                '999': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILOP_R11': {
            'start': 209,
            'end': 210,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'Zero to 3 months (plural delivery)',
                '01': '4 to 11 months',
                '02': '12 to 17 months',
                '03': '18 to 23 months',
                '04': '24 to 35 months',
                '05': '36 to 47 months',
                '06': '48 to 59 months',
                '07': '60 to 71 months',
                '08': '72 months and over',
                '88': 'Not applicable (1st live birth)',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILP_R': {
            'start': 214,
            'end': 216,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '888': 'Not applicable / 1st live birth',
                '999': '999 Unknown or not stated',
            }
        },
        'ILP_R11': {
            'start': 217,
            'end': 218,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'Zero to 3 months (plural delivery)',
                '01': '4 to 11 months',
                '02': '12 to 17 months',
                '03': '18 to 23 months',
                '04': '24 to 35 months',
                '05': '36 to 47 months',
                '06': '48 to 59 months',
                '07': '60 to 71 months',
                '08': '72 months and over',
                '88': 'Not applicable (1st live birth)',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'PRECARE': {
            'start': 224,
            'end': 225,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'No prenatal care',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'F_MPCB': {
            'start': 226,
            'end': 226,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'PRECARE5': {
            'start': 227,
            'end': 227,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': '1st to 3rd month',
                '2': '4th to 6th month',
                '3': '7th to final month',
                '4': 'No prenatal care',
                '5': constants.UNKNOWN_NOT_STATED,
            }
        },
        'PREVIS': {
            'start': 238,
            'end': 239,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-98': '[value] prenatal visits',
                '99': constants.UNKNOWN_NOT_STATED,
                # '*': '[value] prenatal visits',
            }
        },
        'PREVIS_REC': {
            'start': 242,
            'end': 243,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': 'No visits',
                '02': '1 to 2 visits',
                '03': '3 to 4 visits',
                '04': '5 to 6 visits',
                '05': '7 to 8 visits',
                '06': '9 to 10 visits',
                '07': '11 to 12 visits',
                '08': '13 to 14 visits',
                '09': '15 to 16 visits',
                '10': '17 to 18 visits',
                '11': '19 or more visits',
                '12': constants.UNKNOWN_NOT_STATED,
            }
        },
        'F_TPCV': {
            'start': 244,
            'end': 244,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'WIC': {
            'start': 251,
            'end': 251,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_WIC': {
            'start': 252,
            'end': 252,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'CIG_0': {
            'start': 253,
            'end': 254,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG_1': {
            'start': 255,
            'end': 256,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG_2': {
            'start': 257,
            'end': 258,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG_3': {
            'start': 259,
            'end': 260,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG0_R': {
            'start': 261,
            'end': 261,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'CIG1_R': {
            'start': 262,
            'end': 262,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'CIG2_R': {
            'start': 263,
            'end': 263,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'CIG3_R': {
            'start': 264,
            'end': 264,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'F_CIGS_0': {
            'start': 265,
            'end': 265,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CIGS_1': {
            'start': 266,
            'end': 266,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CIGS_2': {
            'start': 267,
            'end': 267,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CIGS_3': {
            'start': 268,
            'end': 268,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'CIG_REC': {
            'start': 269,
            'end': 269,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_TOBACO': {
            'start': 270,
            'end': 270,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'M_Ht_In': {
            'start': 280,
            'end': 281,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '30-78': '[value] inches',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_M_HT': {
            'start': 282,
            'end': 282,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'BMI': {
            'start': 283,
            'end': 286,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99.9': constants.UNKNOWN_NOT_STATED
            }
        },
        'BMI_R': {
            'start': 287,
            'end': 287,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Underweight <18.5',
                '2': 'Normal 18.5-24.9',
                '3': 'Overweight 25.0-29.9',
                '4': 'Obesity I 35.0-34.9',
                '5': 'Obesity II 35.0-39.9',
                '6': 'Extreme Obesity III equal or more than 40.0',
                '9': 'Unknown or not stated',
            }
        },
        'PWgt_R': {
            'start': 292,
            'end': 294,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '75-375': '[value] lbs.',
                '999': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_PWGT': {
            'start': 295,
            'end': 295,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'DWgt_R': {
            'start': 301,
            'end': 299,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '100-400': '[value] lbs.',
                '999': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_DWGT': {
            'start': 303,
            'end': 303,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'WTGAIN': {
            'start': 304,
            'end': 305,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-97': '[value] lbs.',
                '98': '98 pounds and over',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'WTGAIN_REC': {
            'start': 306,
            'end': 306,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Less than 11 pounds',
                '2': '11 to 20 pounds',
                '3': '21 to 30 pounds',
                '4': '31 to 40 pounds',
                '5': '41 to 98 pounds',
                '9': 'Unknown or not stated',
            }
        },
        'F_WTGAIN': {
            'start': 307,
            'end': 307,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RF_PDIAB': {
            'start': 313,
            'end': 313,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_GDIAB': {
            'start': 314,
            'end': 314,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_PHYPE': {
            'start': 315,
            'end': 315,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_GHYPE': {
            'start': 316,
            'end': 316,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_EHYPE': {
            'start': 317,
            'end': 317,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_PPTERM': {
            'start': 318,
            'end': 318,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_RF_PDIAB': {
            'start': 319,
            'end': 319,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_GDIAB': {
            'start': 320,
            'end': 320,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_PHYPER': {
            'start': 321,
            'end': 321,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_GHYPER': {
            'start': 322,
            'end': 322,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_ECLAMP': {
            'start': 323,
            'end': 323,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_PPB': {
            'start': 324,
            'end': 324,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RF_INFTR': {
            'start': 325,
            'end': 325,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_FEDRG': {
            'start': 326,
            'end': 326,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'RF_ARTEC': {
            'start': 327,
            'end': 327,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'F_RF_INFT': {
            'start': 328,
            'end': 328,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_INF_ART': {
            'start': 329,
            'end': 329,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_INF_DRG': {
            'start': 330,
            'end': 330,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RF_CESAR': {
            'start': 331,
            'end': 331,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_CESARN': {
            'start': 332,
            'end': 333,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'None',
                '01-30': '[value] previous cesareans',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_RF_CESAR': {
            'start': 335,
            'end': 335,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_NCESAR': {
            'start': 336,
            'end': 336,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_RISKS': {
            'start': 337,
            'end': 337,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'IP_GON': {
            'start': 343,
            'end': 343,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_SYPH': {
            'start': 344,
            'end': 344,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_CHLAM': {
            'start': 345,
            'end': 345,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_HEPB': {
            'start': 346,
            'end': 346,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_HEPC': {
            'start': 347,
            'end': 347,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_IP_GONOR': {
            'start': 348,
            'end': 348,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_SYPH': {
            'start': 349,
            'end': 349,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_CHLAM': {
            'start': 350,
            'end': 350,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_HEPATB': {
            'start': 351,
            'end': 351,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_HEPATC': {
            'start': 352,
            'end': 352,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_INFEC': {
            'start': 353,
            'end': 353,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'OB_ECVS': {
            'start': 360,
            'end': 360,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'OB_ECVF': {
            'start': 361,
            'end': 361,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_OB_SUCC': {
            'start': 363,
            'end': 363,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_OB_FAIL': {
            'start': 364,
            'end': 364,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'LD_INDL': {
            'start': 383,
            'end': 383,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_AUGM': {
            'start': 384,
            'end': 384,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_STER': {
            'start': 385,
            'end': 385,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_ANTB': {
            'start': 386,
            'end': 386,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_CHOR': {
            'start': 387,
            'end': 387,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_ANES': {
            'start': 388,
            'end': 388,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_LD_INDL': {
            'start': 389,
            'end': 389,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_AUGM': {
            'start': 390,
            'end': 390,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_STER': {
            'start': 391,
            'end': 391,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_ANTB': {
            'start': 392,
            'end': 392,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_CHOR': {
            'start': 393,
            'end': 393,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_ANES': {
            'start': 394,
            'end': 394,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_LBRDLV': {
            'start': 395,
            'end': 395,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'ME_PRES': {
            'start': 401,
            'end': 401,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Cephalic',
                '2': 'Breech',
                '3': 'Other',
                '9': 'Unknown or not stated',
            }
        },
        'ME_ROUT': {
            'start': 402,
            'end': 402,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Spontaneous',
                '2': 'Forceps',
                '3': 'Vacuum',
                '4': 'Cesarean',
                '9': 'Unknown or not stated',

            }
        },
        'ME_TRIAL': {
            'start': 403,
            'end': 403,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'F_ME_PRES': {
            'start': 404,
            'end': 404,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_ME_ROUT': {
            'start': 405,
            'end': 405,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_ME_TRIAL': {
            'start': 406,
            'end': 406,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RDMETH_REC': {
            'start': 407,
            'end': 407,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Vaginal (excludes vaginal after previous C-section)',
                '2': 'Vaginal after previous c-section',
                '3': 'Primary C-section',
                '4': 'Repeat C-section',
                '5': 'Vaginal (unknown if previous c-section)',
                '6': 'C-section (unknown if previous c-section)',
                '9': 'Not stated',
            }
        },
        'DMETH_REC': {
            'start': 408,
            'end': 408,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Vaginal',
                '2': 'C-Section',
                '9': 'Unknown',
            }
        },
        'F_DMETH_REC': {
            'start': 409,
            'end': 409,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'MM_MTR': {
            'start': 415,
            'end': 415,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_PLAC': {
            'start': 416,
            'end': 416,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_RUPT': {
            'start': 417,
            'end': 417,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_UHYST': {
            'start': 418,
            'end': 418,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_AICU': {
            'start': 419,
            'end': 419,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_MM_MTR': {
            'start': 421,
            'end': 421,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_PLAC': {
            'start': 422,
            'end': 422,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_RUPT': {
            'start': 423,
            'end': 423,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_UHYST': {
            'start': 424,
            'end': 424,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_AICU': {
            'start': 425,
            'end': 425,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_MMORB': {
            'start': 427,
            'end': 427,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'ATTEND': {
            'start': 433,
            'end': 433,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Doctor of Medicine (MD)',
                '2': 'Doctor of Osteopathy (DO)',
                '3': 'Certified Nurse Midwife (CNM)',
                '4': 'Other Midwife',
                '5': 'Other',
                '9': constants.UNKNOWN_NOT_STATED,
            }
        },
        'MTRAN': {
            'start': 434,
            'end': 434,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'PAY': {
            'start': 435,
            'end': 435,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Medicaid',
                '2': 'Private Insurance',
                '3': 'Self-Pay',
                '4': 'Indian Health Service',
                '5': 'CHAMPUS/TRICARE',
                '6': 'Other Government (Federal, State, Local)',
                '8': 'Other',
                '9': 'Unknown',
            }
        },
        'PAY_REC': {
            'start': 436,
            'end': 436,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Medicaid',
                '2': 'Private Insurance',
                '3': 'Self Pay',
                '4': 'Other',
                '9': 'Unknown',
            }
        },
        'F_PAY': {
            'start': 437,
            'end': 437,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_PAY_REC': {
            'start': 438,
            'end': 438,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'APGAR5': {
            'start': 444,
            'end': 445,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-10': 'A score of [value]',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'APGAR5R': {
            'start': 446,
            'end': 446,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'A score of 0-3',
                '2': 'A score of 4-6',
                '3': 'A score of 7-8',
                '4': 'A score of 9-10',
                '5': 'Unknown or not stated',
            }
        },
        'F_APGAR5': {
            'start': 447,
            'end': 447,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'APGAR10': {
            'start': 448,
            'end': 449,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-10': 'A score of [value]',
                '88': 'Not applicable',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'APGAR10R': {
            'start': 450,
            'end': 450,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'A score of 0-3',
                '2': 'A score of 4-6',
                '3': 'A score of 7-8',
                '4': 'A score of 9-10',
                '5': 'Not stated/not applicable',
            }
        },
        'DPLURAL': {
            'start': 454,
            'end': 454,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Single',
                '2': 'Twin',
                '3': 'Triplet',
                '4': 'Quadruplet',
                '5': 'Quintuplet or higher',
            }
        },
        'IMP_PLUR': {
            'start': 456,
            'end': 456,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Plurality is imputed',
                '1': 'Plurality is not imputed',
            }
        },
        'SETORDER_R': {
            'start': 459,
            'end': 459,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': '1st',
                '2': '2nd',
                '3': '3rd',
                '4': '4th',
                '5': '5th to 16th',
                '9': 'Unknown or not stated',
            }
        },
        'SEX': {
            'start': 475,
            'end': 475,
            'value': None,
            'definition': None,
            'valueDefinition': {
                'M': 'Male',
                'F': 'Female',
            }
        },
        'IMP_SEX': {
            'start': 476,
            'end': 476,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Infant Sex not Imputed',
                '1': 'Infant Sex is Imputed',
            }
        },
        'DLMP_MM': {
            'start': 477,
            'end': 478,
            'value': None,
            'definition': None,
            'valueDefinition': constants.MONTH
        },
        'DLMP_YY': {
            'start': 481,
            'end': 484,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '9999': constants.UNKNOWN_NOT_STATED,
                '*': 'Year [value] of last normal menses',
            }
        },
        'COMPGST_IMP': {
            'start': 488,
            'end': 488,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Combined Gestation is not imputed',
                '1': 'Combined Gestation is imputed',
            }
        },
        'OBGEST_FLG': {
            'start': 489,
            'end': 489,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Obstetric Estimate is not used',
                '1': 'Obstetric Estimate is used',
            }
        },
        'COMBGEST': {
            'start': 490,
            'end': 491,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '17-47': 'Week [value] of Gestation',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'GESTREC10': {
            'start': 492,
            'end': 493,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': 'Under 20 weeks',
                '02': '20-27 weeks',
                '03': '28-31 weeks',
                '04': '32-33 weeks',
                '05': '34-36 weeks',
                '06': '37-38 weeks',
                '07': '39 weeks',
                '08': '40 weeks',
                '09': '41 weeks',
                '10': '42 weeks and over',
                '99': 'Unknown',
            }
        },
        'GESTREC3': {
            'start': 494,
            'end': 494,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Under 37 weeks',
                '2': '37 weeks and over',
                '3': 'Not stated',
            }
        },
        'LMPUSED': {
            'start': 498,
            'end': 498,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Combined gestation not used',
                '1': 'Combined gestation used',
            }
        },
        'OEGest_Comb': {
            'start': 499,
            'end': 500,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '17-47': '[value] weeks of gestation',
                '99': 'Not stated',
            }
        },
        'OEGest_R10': {
            'start': 501,
            'end': 502,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': 'Under 20 weeks',
                '02': '20-27 weeks',
                '03': '28-31 weeks',
                '04': '32-33 weeks',
                '05': '34-36 weeks',
                '06': '37-38 weeks',
                '07': '39 weeks',
                '08': '40 weeks',
                '09': '41 weeks',
                '10': '42 weeks and over',
                '99': 'Unknown',
            }
        },
        'OEGest_R3': {
            'start': 503,
            'end': 503,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Under 37 weeks',
                '2': '37 weeks and over',
                '3': 'Not stated',
            }
        },
        'DBWT': {
            'start': 504,
            'end': 507,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '0227-8165': '[value] grams',
                '9999': 'Not stated birth weigh',
            }
        },
        'BWTR12': {
            'start': 509,
            'end': 510,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': '0227 - 0499 grams',
                '02': '0500 - 0999 grams',
                '03': '1000 - 1499 grams',
                '04': '1500 - 1999 grams',
                '05': '2000 - 2499 grams',
                '06': '2500 - 2999 grams',
                '07': '3000 - 3499 grams',
                '08': '3500 - 3999 grams',
                '09': '4000 - 4499 grams',
                '10': '4500 - 4999 grams',
                '11': '5000 - 8165 grams',
                '12': 'Not Stated ',
            }
        },
        'BWTR4': {
            'start': 511,
            'end': 511,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': '0227 - 1499 grams',
                '2': '1500 - 2499 grams',
                '3': '2500 - 8165 grams',
                '4': constants.UNKNOWN_NOT_STATED,
            }
        },
        'AB_AVEN1': {
            'start': 517,
            'end': 517,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_AVEN6': {
            'start': 518,
            'end': 518,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_NICU': {
            'start': 519,
            'end': 519,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_SURF': {
            'start': 520,
            'end': 520,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_ANTI': {
            'start': 521,
            'end': 521,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_SEIZ': {
            'start': 522,
            'end': 522,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_AB_VENT': {
            'start': 524,
            'end': 524,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_VENT6': {
            'start': 525,
            'end': 525,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_NIUC': {
            'start': 526,
            'end': 526,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_SURFAC': {
            'start': 527,
            'end': 527,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_ANTIBIO': {
            'start': 528,
            'end': 528,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_SEIZ': {
            'start': 529,
            'end': 529,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_ABNORM': {
            'start': 531,
            'end': 531,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'CA_ANEN': {
            'start': 537,
            'end': 537,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_MNSB': {
            'start': 538,
            'end': 538,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CCHD': {
            'start': 539,
            'end': 539,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CDH': {
            'start': 540,
            'end': 540,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_OMPH': {
            'start': 541,
            'end': 541,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_GAST': {
            'start': 542,
            'end': 542,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_CA_ANEN': {
            'start': 543,
            'end': 543,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_MENIN': {
            'start': 544,
            'end': 544,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_HEART': {
            'start': 545,
            'end': 545,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_HERNIA': {
            'start': 546,
            'end': 546,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_OMPHA': {
            'start': 547,
            'end': 547,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_GASTRO': {
            'start': 548,
            'end': 548,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'CA_LIMB': {
            'start': 549,
            'end': 549,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CLEFT': {
            'start': 550,
            'end': 550,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CLPAL': {
            'start': 551,
            'end': 551,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_DOWN': {
            'start': 552,
            'end': 552,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_DISOR': {
            'start': 553,
            'end': 553,
            'value': None,
            'definition': None,
            'valueDefinition': {
                'C': 'Confirmed',
                'P': 'Pending',
                'N': 'No',
                'U': 'Unknown',
            }
        },
        'CA_HYPO': {
            'start': 554,
            'end': 554,
            'value': None,
            'definition': None,
            'valueDefinition': {
                'Y': 'Yes, anomaly reported',
                'N': 'No, anomaly not reported',
                'U': 'Unknown',
            }
        },
        'F_CA_LIMB': {
            'start': 555,
            'end': 555,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_CLEFTLP': {
            'start': 556,
            'end': 556,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_CLEFT': {
            'start': 557,
            'end': 557,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_DOWNS': {
            'start': 558,
            'end': 558,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_CHROM': {
            'start': 559,
            'end': 559,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_HYPOS': {
            'start': 560,
            'end': 560,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_CONGEN': {
            'start': 561,
            'end': 561,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'ITRAN': {
            'start': 567,
            'end': 567,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'ILIVE': {
            'start': 568,
            'end': 568,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'BFED': {
            'start': 569,
            'end': 569,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_BFED': {
            'start': 570,
            'end': 570,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        } 
    },
    '2017': {
        'DOB_YY': {
            'start': 9,
            'end': 12,
            'value': None,
            'definition': None
        },
        'DOB_MM': {
            'start': 13,
            'end': 14,
            'value': None,
            'definition': None,
            'valueDefinition': constants.MONTH
        },
        'DOB_TT': {
            'start': 19,
            'end': 22,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '9999': 'Not Stated',
            }
        },
        'DOB_WK': {
            'start': 23,
            'end': 23,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Sunday',
                '2': 'Monday',
                '3': 'Tuesday',
                '4': 'Wednesday',
                '5': 'Thursday',
                '6': 'Friday',
                '7': 'Saturday',
            }
        },
        'BFACIL': {
            'start': 32,
            'end': 32,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Hospital',
                '2': 'Freestanding Birth Center',
                '3': 'Home (intended)',
                '4': 'Home (not intended)',
                '5': 'Home (unknown if intended)',
                '6': 'Clinic / Doctor\'s Office',
                '7': 'Other',
                '9': 'Unknown',
            }
        },
        'F_FACILITY': {
            'start': 33,
            'end': 33,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'BFACIL3': {
            'start': 50,
            'end': 50,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'In Hospital',
                '2': 'Not in Hospital',
                '3': constants.UNKNOWN_NOT_STATED,
            }
        },
        'MAGE_IMPFLG': {
            'start': 73,
            'end': 73,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Age not imputed',
                '1': 'Age imputed',
            }
        },
        'MAGE_REPFLG': {
            'start': 74,
            'end': 74,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Reported age not used',
                '1': 'Reported age used',
            }
        },
        'MAGER': {
            'start': 75,
            'end': 76,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE
        },
        'MAGER14': {
            'start': 77,
            'end': 78,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE14
        },
        'MAGER9': {
            'start': 79,
            'end': 79,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE9
        },
        'MBSTATE_REC': {
            'start': 84,
            'end': 84,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Born in the U.S. (50 US States)',
                '2': 'Born outside the U.S. (includes possessions)',
                '3': constants.UNKNOWN_NOT_STATED,
            }
        },
        'RESTATUS': {
            'start': 104,
            'end': 104,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '__MBSTATE_REC': {
                    '1': {
                        '1': 'RESIDENT: State and county of occurrence and residence are the same.',
                        '2': 'INTRASTATE NONRESIDENT: State of occurrence and residence are the same but county is different.',
                        '3': 'INTERSTATE NONRESIDENT: State of occurrence and residence are different but both are one of the 50 US states or District of Columbia.',
                        '4': 'FOREIGN RESIDENT: The state of residence is not one of the 50 US states or District of Columbia.',
                    },
                    '2': {
                        '1': 'RESIDENT: State and county of occurrence and residence  residence are the same. (Unique to Guam, all US residents are considered residents of Guam and thus are assigned 1.)',
                        '2': 'INTRATERRITORY NONRESIDENT: Territory of occurrence and residence are the same but county is different.',
                        '3': 'INTERTERRITORY RESIDENT: Territory of occurrence and residence are different but both are US Territories.',
                        '4': 'FOREIGN RESIDENT: The residence is not a US Territory.',
                    }
                }
            }
        },
        'MRACE31': {
            'start': 105,
            'end': 106,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE31
        },
        'MRACE6': {
            'start': 107,
            'end': 107,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE6
        },
        'MRACE15': {
            'start': 108,
            'end': 109,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE15
        },
        'MBRACE': {
            'start': 110,
            'end': 110,
            'value': None,
            'definition': None,
            'valueDefinition': constants.BRACE
        },
        'MRACEIMP': {
            'start': 111,
            'end': 111,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Mother\'s race not imputed',
                '1': 'Unknown race imputed',
                '2': 'All other races, formerly coded 09, imputed.',
            }
        },
        'MHISP_R': {
            'start': 115,
            'end': 115,
            'value': None,
            'definition': None,
            'valueDefinition': constants.HISP_R
        },
        'F_MHISP': {
            'start': 116,
            'end': 116,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'MRACEHISP': {
            'start': 117,
            'end': 117,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE_HISP
        },
        'MAR_P': {
            'start': 119,
            'end': 119,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'DMAR': { #X
            'start': 120,
            'end': 120,
            'value': None,
            'definition': None,
            # 'valueDefinition': {
            # }
        },
        'MAR_IMP': {
            'start': 121,
            'end': 121,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Marital Status not imputed',
                '1': 'Marital Status imputed',
            }
        },
        'F_MAR_P': {
            'start': 123,
            'end': 123,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'MEDUC': {
            'start': 124,
            'end': 124,
            'value': None,
            'definition': None,
            'valueDefinition': constants.EDUC
        },
        'F_MEDUC': {
            'start': 126,
            'end': 126,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'FAGERPT_FLG': {
            'start': 142,
            'end': 142,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Father\'s reported age not used',
                '1': 'Father\'s reported age used',
            }
        },
        'FAGECOMB': {
            'start': 147,
            'end': 148,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'FAGEREC11': {
            'start': 149,
            'end': 150,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE11
        },
        'FRACE31': {
            'start': 151,
            'end': 152,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE31
        },
        'FRACE6': {
            'start': 153,
            'end': 153,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE6
        },
        'FRACE15': {
            'start': 154,
            'end': 155,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE15
        },
        'FHISP_R': {
            'start': 160,
            'end': 160,
            'value': None,
            'definition': None,
            'valueDefinition': constants.HISP_R
        },
        'F_FHISP': {
            'start': 161,
            'end': 161,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'FRACEHISP': {
            'start': 162,
            'end': 162,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE_HISP
        },
        'FEDUC': {
            'start': 163,
            'end': 163,
            'value': None,
            'definition': None,
            'valueDefinition': constants.EDUC
        },
        'F_FEDUC': {
            'start': 165,
            'end': 165,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'PRIORLIVE': {
            'start': 171,
            'end': 172,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'PRIORDEAD': {
            'start': 173,
            'end': 174,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'PRIORTERM': {
            'start': 175,
            'end': 176,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'LBO_REC': {
            'start': 179,
            'end': 179,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '8': '8 or more live births',
                '9': constants.UNKNOWN_NOT_STATED,
            }
        },
        'TBO_REC': {
            'start': 182,
            'end': 182,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '8': '8 or more live births',
                '9': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILLB_R': {
            'start': 198,
            'end': 200,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '888': 'Not applicable / 1st live birth',
                '999': '999 Unknown or not stated',
            }
        },
        'ILLB_R11': {
            'start': 201,
            'end': 202,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'Zero to 3 months (plural delivery)',
                '01': '4 to 11 months',
                '02': '12 to 17 months',
                '03': '18 to 23 months',
                '04': '24 to 35 months',
                '05': '36 to 47 months',
                '06': '48 to 59 months',
                '07': '60 to 71 months',
                '08': '72 months and over',
                '88': 'Not applicable (1st live birth)',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILOP_R': {
            'start': 206,
            'end': 208,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '888': 'Not applicable / 1st live birth',
                '999': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILOP_R11': {
            'start': 209,
            'end': 210,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'Zero to 3 months (plural delivery)',
                '01': '4 to 11 months',
                '02': '12 to 17 months',
                '03': '18 to 23 months',
                '04': '24 to 35 months',
                '05': '36 to 47 months',
                '06': '48 to 59 months',
                '07': '60 to 71 months',
                '08': '72 months and over',
                '88': 'Not applicable (1st live birth)',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILP_R': {
            'start': 214,
            'end': 216,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '888': 'Not applicable / 1st live birth',
                '999': '999 Unknown or not stated',
            }
        },
        'ILP_R11': {
            'start': 217,
            'end': 218,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'Zero to 3 months (plural delivery)',
                '01': '4 to 11 months',
                '02': '12 to 17 months',
                '03': '18 to 23 months',
                '04': '24 to 35 months',
                '05': '36 to 47 months',
                '06': '48 to 59 months',
                '07': '60 to 71 months',
                '08': '72 months and over',
                '88': 'Not applicable (1st live birth)',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'PRECARE': {
            'start': 224,
            'end': 225,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'No prenatal care',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'F_MPCB': {
            'start': 226,
            'end': 226,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'PRECARE5': {
            'start': 227,
            'end': 227,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': '1st to 3rd month',
                '2': '4th to 6th month',
                '3': '7th to final month',
                '4': 'No prenatal care',
                '5': constants.UNKNOWN_NOT_STATED,
            }
        },
        'PREVIS': {
            'start': 238,
            'end': 239,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-98': '[value] prenatal visits',
                '99': constants.UNKNOWN_NOT_STATED,
                # '*': '[value] prenatal visits',
            }
        },
        'PREVIS_REC': {
            'start': 242,
            'end': 243,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': 'No visits',
                '02': '1 to 2 visits',
                '03': '3 to 4 visits',
                '04': '5 to 6 visits',
                '05': '7 to 8 visits',
                '06': '9 to 10 visits',
                '07': '11 to 12 visits',
                '08': '13 to 14 visits',
                '09': '15 to 16 visits',
                '10': '17 to 18 visits',
                '11': '19 or more visits',
                '12': constants.UNKNOWN_NOT_STATED,
            }
        },
        'F_TPCV': {
            'start': 244,
            'end': 244,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'WIC': {
            'start': 251,
            'end': 251,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_WIC': {
            'start': 252,
            'end': 252,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'CIG_0': {
            'start': 253,
            'end': 254,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG_1': {
            'start': 255,
            'end': 256,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG_2': {
            'start': 257,
            'end': 258,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG_3': {
            'start': 259,
            'end': 260,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG0_R': {
            'start': 261,
            'end': 261,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'CIG1_R': {
            'start': 262,
            'end': 262,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'CIG2_R': {
            'start': 263,
            'end': 263,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'CIG3_R': {
            'start': 264,
            'end': 264,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'F_CIGS_0': {
            'start': 265,
            'end': 265,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CIGS_1': {
            'start': 266,
            'end': 266,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CIGS_2': {
            'start': 267,
            'end': 267,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CIGS_3': {
            'start': 268,
            'end': 268,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'CIG_REC': {
            'start': 269,
            'end': 269,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_TOBACO': {
            'start': 270,
            'end': 270,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'M_Ht_In': {
            'start': 280,
            'end': 281,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '30-78': '[value] inches',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_M_HT': {
            'start': 282,
            'end': 282,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'BMI': {
            'start': 283,
            'end': 286,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99.9': constants.UNKNOWN_NOT_STATED
            }
        },
        'BMI_R': {
            'start': 287,
            'end': 287,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Underweight <18.5',
                '2': 'Normal 18.5-24.9',
                '3': 'Overweight 25.0-29.9',
                '4': 'Obesity I 35.0-34.9',
                '5': 'Obesity II 35.0-39.9',
                '6': 'Extreme Obesity III equal or more than 40.0',
                '9': 'Unknown or not stated',
            }
        },
        'PWgt_R': {
            'start': 292,
            'end': 294,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '75-375': '[value] lbs.',
                '999': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_PWGT': {
            'start': 295,
            'end': 295,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'DWgt_R': {
            'start': 301,
            'end': 299,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '100-400': '[value] lbs.',
                '999': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_DWGT': {
            'start': 303,
            'end': 303,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'WTGAIN': {
            'start': 304,
            'end': 305,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-97': '[value] lbs.',
                '98': '98 pounds and over',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'WTGAIN_REC': {
            'start': 306,
            'end': 306,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Less than 11 pounds',
                '2': '11 to 20 pounds',
                '3': '21 to 30 pounds',
                '4': '31 to 40 pounds',
                '5': '41 to 98 pounds',
                '9': 'Unknown or not stated',
            }
        },
        'F_WTGAIN': {
            'start': 307,
            'end': 307,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RF_PDIAB': {
            'start': 313,
            'end': 313,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_GDIAB': {
            'start': 314,
            'end': 314,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_PHYPE': {
            'start': 315,
            'end': 315,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_GHYPE': {
            'start': 316,
            'end': 316,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_EHYPE': {
            'start': 317,
            'end': 317,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_PPTERM': {
            'start': 318,
            'end': 318,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_RF_PDIAB': {
            'start': 319,
            'end': 319,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_GDIAB': {
            'start': 320,
            'end': 320,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_PHYPER': {
            'start': 321,
            'end': 321,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_GHYPER': {
            'start': 322,
            'end': 322,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_ECLAMP': {
            'start': 323,
            'end': 323,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_PPB': {
            'start': 324,
            'end': 324,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RF_INFTR': {
            'start': 325,
            'end': 325,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_FEDRG': {
            'start': 326,
            'end': 326,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'RF_ARTEC': {
            'start': 327,
            'end': 327,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'F_RF_INFT': {
            'start': 328,
            'end': 328,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_INF_ART': {
            'start': 329,
            'end': 329,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_INF_DRG': {
            'start': 330,
            'end': 330,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RF_CESAR': {
            'start': 331,
            'end': 331,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_CESARN': {
            'start': 332,
            'end': 333,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'None',
                '01-30': '[value] previous cesareans',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_RF_CESAR': {
            'start': 335,
            'end': 335,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_NCESAR': {
            'start': 336,
            'end': 336,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_RISKS': {
            'start': 337,
            'end': 337,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'IP_GON': {
            'start': 343,
            'end': 343,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_SYPH': {
            'start': 344,
            'end': 344,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_CHLAM': {
            'start': 345,
            'end': 345,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_HEPB': {
            'start': 346,
            'end': 346,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_HEPC': {
            'start': 347,
            'end': 347,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_IP_GONOR': {
            'start': 348,
            'end': 348,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_SYPH': {
            'start': 349,
            'end': 349,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_CHLAM': {
            'start': 350,
            'end': 350,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_HEPATB': {
            'start': 351,
            'end': 351,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_HEPATC': {
            'start': 352,
            'end': 352,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_INFEC': {
            'start': 353,
            'end': 353,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'OB_ECVS': {
            'start': 360,
            'end': 360,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'OB_ECVF': {
            'start': 361,
            'end': 361,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_OB_SUCC': {
            'start': 363,
            'end': 363,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_OB_FAIL': {
            'start': 364,
            'end': 364,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'LD_INDL': {
            'start': 383,
            'end': 383,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_AUGM': {
            'start': 384,
            'end': 384,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_STER': {
            'start': 385,
            'end': 385,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_ANTB': {
            'start': 386,
            'end': 386,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_CHOR': {
            'start': 387,
            'end': 387,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_ANES': {
            'start': 388,
            'end': 388,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_LD_INDL': {
            'start': 389,
            'end': 389,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_AUGM': {
            'start': 390,
            'end': 390,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_STER': {
            'start': 391,
            'end': 391,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_ANTB': {
            'start': 392,
            'end': 392,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_CHOR': {
            'start': 393,
            'end': 393,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_ANES': {
            'start': 394,
            'end': 394,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_LBRDLV': {
            'start': 395,
            'end': 395,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'ME_PRES': {
            'start': 401,
            'end': 401,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Cephalic',
                '2': 'Breech',
                '3': 'Other',
                '9': 'Unknown or not stated',
            }
        },
        'ME_ROUT': {
            'start': 402,
            'end': 402,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Spontaneous',
                '2': 'Forceps',
                '3': 'Vacuum',
                '4': 'Cesarean',
                '9': 'Unknown or not stated',

            }
        },
        'ME_TRIAL': {
            'start': 403,
            'end': 403,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'F_ME_PRES': {
            'start': 404,
            'end': 404,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_ME_ROUT': {
            'start': 405,
            'end': 405,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_ME_TRIAL': {
            'start': 406,
            'end': 406,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RDMETH_REC': {
            'start': 407,
            'end': 407,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Vaginal (excludes vaginal after previous C-section)',
                '2': 'Vaginal after previous c-section',
                '3': 'Primary C-section',
                '4': 'Repeat C-section',
                '5': 'Vaginal (unknown if previous c-section)',
                '6': 'C-section (unknown if previous c-section)',
                '9': 'Not stated',
            }
        },
        'DMETH_REC': {
            'start': 408,
            'end': 408,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Vaginal',
                '2': 'C-Section',
                '9': 'Unknown',
            }
        },
        'F_DMETH_REC': {
            'start': 409,
            'end': 409,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'MM_MTR': {
            'start': 415,
            'end': 415,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_PLAC': {
            'start': 416,
            'end': 416,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_RUPT': {
            'start': 417,
            'end': 417,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_UHYST': {
            'start': 418,
            'end': 418,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_AICU': {
            'start': 419,
            'end': 419,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_MM_MTR': {
            'start': 421,
            'end': 421,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_PLAC': {
            'start': 422,
            'end': 422,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_RUPT': {
            'start': 423,
            'end': 423,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_UHYST': {
            'start': 424,
            'end': 424,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_AICU': {
            'start': 425,
            'end': 425,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_MMORB': {
            'start': 427,
            'end': 427,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'ATTEND': {
            'start': 433,
            'end': 433,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Doctor of Medicine (MD)',
                '2': 'Doctor of Osteopathy (DO)',
                '3': 'Certified Nurse Midwife (CNM)',
                '4': 'Other Midwife',
                '5': 'Other',
                '9': constants.UNKNOWN_NOT_STATED,
            }
        },
        'MTRAN': {
            'start': 434,
            'end': 434,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'PAY': {
            'start': 435,
            'end': 435,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Medicaid',
                '2': 'Private Insurance',
                '3': 'Self-Pay',
                '4': 'Indian Health Service',
                '5': 'CHAMPUS/TRICARE',
                '6': 'Other Government (Federal, State, Local)',
                '8': 'Other',
                '9': 'Unknown',
            }
        },
        'PAY_REC': {
            'start': 436,
            'end': 436,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Medicaid',
                '2': 'Private Insurance',
                '3': 'Self Pay',
                '4': 'Other',
                '9': 'Unknown',
            }
        },
        'F_PAY': {
            'start': 437,
            'end': 437,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_PAY_REC': {
            'start': 438,
            'end': 438,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'APGAR5': {
            'start': 444,
            'end': 445,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-10': 'A score of [value]',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'APGAR5R': {
            'start': 446,
            'end': 446,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'A score of 0-3',
                '2': 'A score of 4-6',
                '3': 'A score of 7-8',
                '4': 'A score of 9-10',
                '5': 'Unknown or not stated',
            }
        },
        'F_APGAR5': {
            'start': 447,
            'end': 447,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'APGAR10': {
            'start': 448,
            'end': 449,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-10': 'A score of [value]',
                '88': 'Not applicable',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'APGAR10R': {
            'start': 450,
            'end': 450,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'A score of 0-3',
                '2': 'A score of 4-6',
                '3': 'A score of 7-8',
                '4': 'A score of 9-10',
                '5': 'Not stated/not applicable',
            }
        },
        'DPLURAL': {
            'start': 454,
            'end': 454,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Single',
                '2': 'Twin',
                '3': 'Triplet',
                '4': 'Quadruplet',
                '5': 'Quintuplet or higher',
            }
        },
        'IMP_PLUR': {
            'start': 456,
            'end': 456,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Plurality is imputed',
                '1': 'Plurality is not imputed',
            }
        },
        'SETORDER_R': {
            'start': 459,
            'end': 459,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': '1st',
                '2': '2nd',
                '3': '3rd',
                '4': '4th',
                '5': '5th to 16th',
                '9': 'Unknown or not stated',
            }
        },
        'SEX': {
            'start': 475,
            'end': 475,
            'value': None,
            'definition': None,
            'valueDefinition': {
                'M': 'Male',
                'F': 'Female',
            }
        },
        'IMP_SEX': {
            'start': 476,
            'end': 476,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Infant Sex not Imputed',
                '1': 'Infant Sex is Imputed',
            }
        },
        'DLMP_MM': {
            'start': 477,
            'end': 478,
            'value': None,
            'definition': None,
            'valueDefinition': constants.MONTH
        },
        'DLMP_YY': {
            'start': 481,
            'end': 484,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '9999': constants.UNKNOWN_NOT_STATED,
                '*': 'Year [value] of last normal menses',
            }
        },
        'COMPGST_IMP': {
            'start': 488,
            'end': 488,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Combined Gestation is not imputed',
                '1': 'Combined Gestation is imputed',
            }
        },
        'OBGEST_FLG': {
            'start': 489,
            'end': 489,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Obstetric Estimate is not used',
                '1': 'Obstetric Estimate is used',
            }
        },
        'COMBGEST': {
            'start': 490,
            'end': 491,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '17-47': 'Week [value] of Gestation',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'GESTREC10': {
            'start': 492,
            'end': 493,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': 'Under 20 weeks',
                '02': '20-27 weeks',
                '03': '28-31 weeks',
                '04': '32-33 weeks',
                '05': '34-36 weeks',
                '06': '37-38 weeks',
                '07': '39 weeks',
                '08': '40 weeks',
                '09': '41 weeks',
                '10': '42 weeks and over',
                '99': 'Unknown',
            }
        },
        'GESTREC3': {
            'start': 494,
            'end': 494,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Under 37 weeks',
                '2': '37 weeks and over',
                '3': 'Not stated',
            }
        },
        'LMPUSED': {
            'start': 498,
            'end': 498,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Combined gestation not used',
                '1': 'Combined gestation used',
            }
        },
        'OEGest_Comb': {
            'start': 499,
            'end': 500,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '17-47': '[value] weeks of gestation',
                '99': 'Not stated',
            }
        },
        'OEGest_R10': {
            'start': 501,
            'end': 502,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': 'Under 20 weeks',
                '02': '20-27 weeks',
                '03': '28-31 weeks',
                '04': '32-33 weeks',
                '05': '34-36 weeks',
                '06': '37-38 weeks',
                '07': '39 weeks',
                '08': '40 weeks',
                '09': '41 weeks',
                '10': '42 weeks and over',
                '99': 'Unknown',
            }
        },
        'OEGest_R3': {
            'start': 503,
            'end': 503,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Under 37 weeks',
                '2': '37 weeks and over',
                '3': 'Not stated',
            }
        },
        'DBWT': {
            'start': 504,
            'end': 507,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '0227-8165': '[value] grams',
                '9999': 'Not stated birth weigh',
            }
        },
        'BWTR12': {
            'start': 509,
            'end': 510,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': '0227 - 0499 grams',
                '02': '0500 - 0999 grams',
                '03': '1000 - 1499 grams',
                '04': '1500 - 1999 grams',
                '05': '2000 - 2499 grams',
                '06': '2500 - 2999 grams',
                '07': '3000 - 3499 grams',
                '08': '3500 - 3999 grams',
                '09': '4000 - 4499 grams',
                '10': '4500 - 4999 grams',
                '11': '5000 - 8165 grams',
                '12': 'Not Stated ',
            }
        },
        'BWTR4': {
            'start': 511,
            'end': 511,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': '0227 - 1499 grams',
                '2': '1500 - 2499 grams',
                '3': '2500 - 8165 grams',
                '4': constants.UNKNOWN_NOT_STATED,
            }
        },
        'AB_AVEN1': {
            'start': 517,
            'end': 517,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_AVEN6': {
            'start': 518,
            'end': 518,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_NICU': {
            'start': 519,
            'end': 519,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_SURF': {
            'start': 520,
            'end': 520,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_ANTI': {
            'start': 521,
            'end': 521,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_SEIZ': {
            'start': 522,
            'end': 522,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_AB_VENT': {
            'start': 524,
            'end': 524,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_VENT6': {
            'start': 525,
            'end': 525,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_NIUC': {
            'start': 526,
            'end': 526,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_SURFAC': {
            'start': 527,
            'end': 527,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_ANTIBIO': {
            'start': 528,
            'end': 528,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_SEIZ': {
            'start': 529,
            'end': 529,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_ABNORM': {
            'start': 531,
            'end': 531,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'CA_ANEN': {
            'start': 537,
            'end': 537,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_MNSB': {
            'start': 538,
            'end': 538,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CCHD': {
            'start': 539,
            'end': 539,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CDH': {
            'start': 540,
            'end': 540,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_OMPH': {
            'start': 541,
            'end': 541,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_GAST': {
            'start': 542,
            'end': 542,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_CA_ANEN': {
            'start': 543,
            'end': 543,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_MENIN': {
            'start': 544,
            'end': 544,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_HEART': {
            'start': 545,
            'end': 545,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_HERNIA': {
            'start': 546,
            'end': 546,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_OMPHA': {
            'start': 547,
            'end': 547,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_GASTRO': {
            'start': 548,
            'end': 548,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'CA_LIMB': {
            'start': 549,
            'end': 549,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CLEFT': {
            'start': 550,
            'end': 550,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CLPAL': {
            'start': 551,
            'end': 551,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_DOWN': {
            'start': 552,
            'end': 552,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_DISOR': {
            'start': 553,
            'end': 553,
            'value': None,
            'definition': None,
            'valueDefinition': {
                'C': 'Confirmed',
                'P': 'Pending',
                'N': 'No',
                'U': 'Unknown',
            }
        },
        'CA_HYPO': {
            'start': 554,
            'end': 554,
            'value': None,
            'definition': None,
            'valueDefinition': {
                'Y': 'Yes, anomaly reported',
                'N': 'No, anomaly not reported',
                'U': 'Unknown',
            }
        },
        'F_CA_LIMB': {
            'start': 555,
            'end': 555,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_CLEFTLP': {
            'start': 556,
            'end': 556,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_CLEFT': {
            'start': 557,
            'end': 557,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_DOWNS': {
            'start': 558,
            'end': 558,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_CHROM': {
            'start': 559,
            'end': 559,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_HYPOS': {
            'start': 560,
            'end': 560,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_CONGEN': {
            'start': 561,
            'end': 561,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'ITRAN': {
            'start': 567,
            'end': 567,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'ILIVE': {
            'start': 568,
            'end': 568,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'BFED': {
            'start': 569,
            'end': 569,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_BFED': {
            'start': 570,
            'end': 570,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        } 
    },
    '2018': {
        'DOB_YY': {
            'start': 9,
            'end': 12,
            'value': None,
            'definition': None
        },
        'DOB_MM': {
            'start': 13,
            'end': 14,
            'value': None,
            'definition': None,
            'valueDefinition': constants.MONTH
        },
        'DOB_TT': {
            'start': 19,
            'end': 22,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '9999': 'Not Stated',
            }
        },
        'DOB_WK': {
            'start': 23,
            'end': 23,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Sunday',
                '2': 'Monday',
                '3': 'Tuesday',
                '4': 'Wednesday',
                '5': 'Thursday',
                '6': 'Friday',
                '7': 'Saturday',
            }
        },
        'BFACIL': {
            'start': 32,
            'end': 32,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Hospital',
                '2': 'Freestanding Birth Center',
                '3': 'Home (intended)',
                '4': 'Home (not intended)',
                '5': 'Home (unknown if intended)',
                '6': 'Clinic / Doctor\'s Office',
                '7': 'Other',
                '9': 'Unknown',
            }
        },
        'F_FACILITY': {
            'start': 33,
            'end': 33,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'BFACIL3': {
            'start': 50,
            'end': 50,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'In Hospital',
                '2': 'Not in Hospital',
                '3': constants.UNKNOWN_NOT_STATED,
            }
        },
        'MAGE_IMPFLG': {
            'start': 73,
            'end': 73,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Age not imputed',
                '1': 'Age imputed',
            }
        },
        'MAGE_REPFLG': {
            'start': 74,
            'end': 74,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Reported age not used',
                '1': 'Reported age used',
            }
        },
        'MAGER': {
            'start': 75,
            'end': 76,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE
        },
        'MAGER14': {
            'start': 77,
            'end': 78,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE14
        },
        'MAGER9': {
            'start': 79,
            'end': 79,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE9
        },
        'MBSTATE_REC': {
            'start': 84,
            'end': 84,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Born in the U.S. (50 US States)',
                '2': 'Born outside the U.S. (includes possessions)',
                '3': constants.UNKNOWN_NOT_STATED,
            }
        },
        'RESTATUS': {
            'start': 104,
            'end': 104,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '__MBSTATE_REC': {
                    '1': {
                        '1': 'RESIDENT: State and county of occurrence and residence are the same.',
                        '2': 'INTRASTATE NONRESIDENT: State of occurrence and residence are the same but county is different.',
                        '3': 'INTERSTATE NONRESIDENT: State of occurrence and residence are different but both are one of the 50 US states or District of Columbia.',
                        '4': 'FOREIGN RESIDENT: The state of residence is not one of the 50 US states or District of Columbia.',
                    },
                    '2': {
                        '1': 'RESIDENT: State and county of occurrence and residence  residence are the same. (Unique to Guam, all US residents are considered residents of Guam and thus are assigned 1.)',
                        '2': 'INTRATERRITORY NONRESIDENT: Territory of occurrence and residence are the same but county is different.',
                        '3': 'INTERTERRITORY RESIDENT: Territory of occurrence and residence are different but both are US Territories.',
                        '4': 'FOREIGN RESIDENT: The residence is not a US Territory.',
                    }
                }
            }
        },
        'MRACE31': {
            'start': 105,
            'end': 106,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE31
        },
        'MRACE6': {
            'start': 107,
            'end': 107,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE6
        },
        'MRACE15': {
            'start': 108,
            'end': 109,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE15
        },
        'MBRACE': {
            'start': 110,
            'end': 110,
            'value': None,
            'definition': None,
            'valueDefinition': constants.BRACE
        },
        'MRACEIMP': {
            'start': 111,
            'end': 111,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Mother\'s race not imputed',
                '1': 'Unknown race imputed',
                '2': 'All other races, formerly coded 09, imputed.',
            }
        },
        'MHISPX': {
            'start': 112,
            'end': 112,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '0': 'Non-Hispanic',
                '1': 'Mexican',
                '2': 'Puerto Rican',
                '3': 'Cuban',
                '4': 'Central or South American',
                '5': 'Dominican',
                '6': 'Other and Unknown Hispanic',
                '9': 'Origin unknown or not stated',
            }
        },
        'MHISP_R': {
            'start': 115,
            'end': 115,
            'value': None,
            'definition': None,
            'valueDefinition': constants.HISP_R
        },
        'F_MHISP': {
            'start': 116,
            'end': 116,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'MRACEHISP': {
            'start': 117,
            'end': 117,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE_HISP
        },
        'MAR_P': {
            'start': 119,
            'end': 119,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'DMAR': { #X
            'start': 120,
            'end': 120,
            'value': None,
            'definition': None,
            # 'valueDefinition': {
            # }
        },
        'MAR_IMP': {
            'start': 121,
            'end': 121,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Marital Status not imputed',
                '1': 'Marital Status imputed',
            }
        },
        'F_MAR_P': {
            'start': 123,
            'end': 123,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'MEDUC': {
            'start': 124,
            'end': 124,
            'value': None,
            'definition': None,
            'valueDefinition': constants.EDUC
        },
        'F_MEDUC': {
            'start': 126,
            'end': 126,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'FAGERPT_FLG': {
            'start': 142,
            'end': 142,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Father\'s reported age not used',
                '1': 'Father\'s reported age used',
            }
        },
        'FAGECOMB': {
            'start': 147,
            'end': 148,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'FAGEREC11': {
            'start': 149,
            'end': 150,
            'value': None,
            'definition': None,
            'valueDefinition': constants.AGE11
        },
        'FRACE31': {
            'start': 151,
            'end': 152,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE31
        },
        'FRACE6': {
            'start': 153,
            'end': 153,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE6
        },
        'FRACE15': {
            'start': 154,
            'end': 155,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE15
        },
        'FHISPX': {
            'start': 159,
            'end': 159,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '0': 'Non-Hispanic',
                '1': 'Mexican',
                '2': 'Puerto Rican',
                '3': 'Cuban',
                '4': 'Central or South American',
                '5': 'Dominican',
                '6': 'Other and Unknown Hispanic',
                '9': 'Origin unknown or not stated',
            }
        },
        'FHISP_R': {
            'start': 160,
            'end': 160,
            'value': None,
            'definition': None,
            'valueDefinition': constants.HISP_R
        },
        'F_FHISP': {
            'start': 161,
            'end': 161,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'FRACEHISP': {
            'start': 162,
            'end': 162,
            'value': None,
            'definition': None,
            'valueDefinition': constants.RACE_HISP
        },
        'FEDUC': {
            'start': 163,
            'end': 163,
            'value': None,
            'definition': None,
            'valueDefinition': constants.EDUC
        },
        'F_FEDUC': {
            'start': 165,
            'end': 165,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'PRIORLIVE': {
            'start': 171,
            'end': 172,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'PRIORDEAD': {
            'start': 173,
            'end': 174,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'PRIORTERM': {
            'start': 175,
            'end': 176,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'LBO_REC': {
            'start': 179,
            'end': 179,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '8': '8 or more live births',
                '9': constants.UNKNOWN_NOT_STATED,
            }
        },
        'TBO_REC': {
            'start': 182,
            'end': 182,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '8': '8 or more live births',
                '9': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILLB_R': {
            'start': 198,
            'end': 200,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '888': 'Not applicable / 1st live birth',
                '999': '999 Unknown or not stated',
            }
        },
        'ILLB_R11': {
            'start': 201,
            'end': 202,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'Zero to 3 months (plural delivery)',
                '01': '4 to 11 months',
                '02': '12 to 17 months',
                '03': '18 to 23 months',
                '04': '24 to 35 months',
                '05': '36 to 47 months',
                '06': '48 to 59 months',
                '07': '60 to 71 months',
                '08': '72 months and over',
                '88': 'Not applicable (1st live birth)',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILOP_R': {
            'start': 206,
            'end': 208,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '888': 'Not applicable / 1st live birth',
                '999': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILOP_R11': {
            'start': 209,
            'end': 210,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'Zero to 3 months (plural delivery)',
                '01': '4 to 11 months',
                '02': '12 to 17 months',
                '03': '18 to 23 months',
                '04': '24 to 35 months',
                '05': '36 to 47 months',
                '06': '48 to 59 months',
                '07': '60 to 71 months',
                '08': '72 months and over',
                '88': 'Not applicable (1st live birth)',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'ILP_R': {
            'start': 214,
            'end': 216,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '888': 'Not applicable / 1st live birth',
                '999': '999 Unknown or not stated',
            }
        },
        'ILP_R11': {
            'start': 217,
            'end': 218,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'Zero to 3 months (plural delivery)',
                '01': '4 to 11 months',
                '02': '12 to 17 months',
                '03': '18 to 23 months',
                '04': '24 to 35 months',
                '05': '36 to 47 months',
                '06': '48 to 59 months',
                '07': '60 to 71 months',
                '08': '72 months and over',
                '88': 'Not applicable (1st live birth)',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'PRECARE': {
            'start': 224,
            'end': 225,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'No prenatal care',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'F_MPCB': {
            'start': 226,
            'end': 226,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'PRECARE5': {
            'start': 227,
            'end': 227,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': '1st to 3rd month',
                '2': '4th to 6th month',
                '3': '7th to final month',
                '4': 'No prenatal care',
                '5': constants.UNKNOWN_NOT_STATED,
            }
        },
        'PREVIS': {
            'start': 238,
            'end': 239,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-98': '[value] prenatal visits',
                '99': constants.UNKNOWN_NOT_STATED,
                # '*': '[value] prenatal visits',
            }
        },
        'PREVIS_REC': {
            'start': 242,
            'end': 243,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': 'No visits',
                '02': '1 to 2 visits',
                '03': '3 to 4 visits',
                '04': '5 to 6 visits',
                '05': '7 to 8 visits',
                '06': '9 to 10 visits',
                '07': '11 to 12 visits',
                '08': '13 to 14 visits',
                '09': '15 to 16 visits',
                '10': '17 to 18 visits',
                '11': '19 or more visits',
                '12': constants.UNKNOWN_NOT_STATED,
            }
        },
        'F_TPCV': {
            'start': 244,
            'end': 244,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'WIC': {
            'start': 251,
            'end': 251,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_WIC': {
            'start': 252,
            'end': 252,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'CIG_0': {
            'start': 253,
            'end': 254,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG_1': {
            'start': 255,
            'end': 256,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG_2': {
            'start': 257,
            'end': 258,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG_3': {
            'start': 259,
            'end': 260,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG
        },
        'CIG0_R': {
            'start': 261,
            'end': 261,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'CIG1_R': {
            'start': 262,
            'end': 262,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'CIG2_R': {
            'start': 263,
            'end': 263,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'CIG3_R': {
            'start': 264,
            'end': 264,
            'value': None,
            'definition': None,
            'valueDefinition': constants.CIG_R
        },
        'F_CIGS_0': {
            'start': 265,
            'end': 265,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CIGS_1': {
            'start': 266,
            'end': 266,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CIGS_2': {
            'start': 267,
            'end': 267,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CIGS_3': {
            'start': 268,
            'end': 268,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'CIG_REC': {
            'start': 269,
            'end': 269,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_TOBACO': {
            'start': 270,
            'end': 270,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'M_Ht_In': {
            'start': 280,
            'end': 281,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '30-78': '[value] inches',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_M_HT': {
            'start': 282,
            'end': 282,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'BMI': {
            'start': 283,
            'end': 286,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '99.9': constants.UNKNOWN_NOT_STATED
            }
        },
        'BMI_R': {
            'start': 287,
            'end': 287,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Underweight <18.5',
                '2': 'Normal 18.5-24.9',
                '3': 'Overweight 25.0-29.9',
                '4': 'Obesity I 35.0-34.9',
                '5': 'Obesity II 35.0-39.9',
                '6': 'Extreme Obesity III equal or more than 40.0',
                '9': 'Unknown or not stated',
            }
        },
        'PWgt_R': {
            'start': 292,
            'end': 294,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '75-375': '[value] lbs.',
                '999': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_PWGT': {
            'start': 295,
            'end': 295,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'DWgt_R': {
            'start': 301,
            'end': 299,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '100-400': '[value] lbs.',
                '999': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_DWGT': {
            'start': 303,
            'end': 303,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'WTGAIN': {
            'start': 304,
            'end': 305,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-97': '[value] lbs.',
                '98': '98 pounds and over',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'WTGAIN_REC': {
            'start': 306,
            'end': 306,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Less than 11 pounds',
                '2': '11 to 20 pounds',
                '3': '21 to 30 pounds',
                '4': '31 to 40 pounds',
                '5': '41 to 98 pounds',
                '9': 'Unknown or not stated',
            }
        },
        'F_WTGAIN': {
            'start': 307,
            'end': 307,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RF_PDIAB': {
            'start': 313,
            'end': 313,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_GDIAB': {
            'start': 314,
            'end': 314,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_PHYPE': {
            'start': 315,
            'end': 315,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_GHYPE': {
            'start': 316,
            'end': 316,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_EHYPE': {
            'start': 317,
            'end': 317,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_PPTERM': {
            'start': 318,
            'end': 318,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_RF_PDIAB': {
            'start': 319,
            'end': 319,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_GDIAB': {
            'start': 320,
            'end': 320,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_PHYPER': {
            'start': 321,
            'end': 321,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_GHYPER': {
            'start': 322,
            'end': 322,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_ECLAMP': {
            'start': 323,
            'end': 323,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_PPB': {
            'start': 324,
            'end': 324,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RF_INFTR': {
            'start': 325,
            'end': 325,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_FEDRG': {
            'start': 326,
            'end': 326,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'RF_ARTEC': {
            'start': 327,
            'end': 327,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'F_RF_INFT': {
            'start': 328,
            'end': 328,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_INF_ART': {
            'start': 329,
            'end': 329,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_INF_DRG': {
            'start': 330,
            'end': 330,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RF_CESAR': {
            'start': 331,
            'end': 331,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'RF_CESARN': {
            'start': 332,
            'end': 333,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00': 'None',
                '01-30': '[value] previous cesareans',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'F_RF_CESAR': {
            'start': 335,
            'end': 335,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_RF_NCESAR': {
            'start': 336,
            'end': 336,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_RISKS': {
            'start': 337,
            'end': 337,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'IP_GON': {
            'start': 343,
            'end': 343,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_SYPH': {
            'start': 344,
            'end': 344,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_CHLAM': {
            'start': 345,
            'end': 345,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_HEPB': {
            'start': 346,
            'end': 346,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'IP_HEPC': {
            'start': 347,
            'end': 347,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_IP_GONOR': {
            'start': 348,
            'end': 348,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_SYPH': {
            'start': 349,
            'end': 349,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_CHLAM': {
            'start': 350,
            'end': 350,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_HEPATB': {
            'start': 351,
            'end': 351,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_IP_HEPATC': {
            'start': 352,
            'end': 352,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_INFEC': {
            'start': 353,
            'end': 353,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'OB_ECVS': {
            'start': 360,
            'end': 360,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'OB_ECVF': {
            'start': 361,
            'end': 361,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_OB_SUCC': {
            'start': 363,
            'end': 363,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_OB_FAIL': {
            'start': 364,
            'end': 364,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'LD_INDL': {
            'start': 383,
            'end': 383,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_AUGM': {
            'start': 384,
            'end': 384,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_STER': {
            'start': 385,
            'end': 385,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_ANTB': {
            'start': 386,
            'end': 386,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_CHOR': {
            'start': 387,
            'end': 387,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'LD_ANES': {
            'start': 388,
            'end': 388,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_LD_INDL': {
            'start': 389,
            'end': 389,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_AUGM': {
            'start': 390,
            'end': 390,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_STER': {
            'start': 391,
            'end': 391,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_ANTB': {
            'start': 392,
            'end': 392,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_CHOR': {
            'start': 393,
            'end': 393,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_LD_ANES': {
            'start': 394,
            'end': 394,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_LBRDLV': {
            'start': 395,
            'end': 395,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'ME_PRES': {
            'start': 401,
            'end': 401,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Cephalic',
                '2': 'Breech',
                '3': 'Other',
                '9': 'Unknown or not stated',
            }
        },
        'ME_ROUT': {
            'start': 402,
            'end': 402,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Spontaneous',
                '2': 'Forceps',
                '3': 'Vacuum',
                '4': 'Cesarean',
                '9': 'Unknown or not stated',

            }
        },
        'ME_TRIAL': {
            'start': 403,
            'end': 403,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNUX
        },
        'F_ME_PRES': {
            'start': 404,
            'end': 404,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_ME_ROUT': {
            'start': 405,
            'end': 405,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_ME_TRIAL': {
            'start': 406,
            'end': 406,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'RDMETH_REC': {
            'start': 407,
            'end': 407,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Vaginal (excludes vaginal after previous C-section)',
                '2': 'Vaginal after previous c-section',
                '3': 'Primary C-section',
                '4': 'Repeat C-section',
                '5': 'Vaginal (unknown if previous c-section)',
                '6': 'C-section (unknown if previous c-section)',
                '9': 'Not stated',
            }
        },
        'DMETH_REC': {
            'start': 408,
            'end': 408,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Vaginal',
                '2': 'C-Section',
                '9': 'Unknown',
            }
        },
        'F_DMETH_REC': {
            'start': 409,
            'end': 409,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'MM_MTR': {
            'start': 415,
            'end': 415,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_PLAC': {
            'start': 416,
            'end': 416,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_RUPT': {
            'start': 417,
            'end': 417,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_UHYST': {
            'start': 418,
            'end': 418,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'MM_AICU': {
            'start': 419,
            'end': 419,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_MM_MTR': {
            'start': 421,
            'end': 421,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_PLAC': {
            'start': 422,
            'end': 422,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_RUPT': {
            'start': 423,
            'end': 423,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_UHYST': {
            'start': 424,
            'end': 424,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_MM_AICU': {
            'start': 425,
            'end': 425,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_MMORB': {
            'start': 427,
            'end': 427,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'ATTEND': {
            'start': 433,
            'end': 433,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Doctor of Medicine (MD)',
                '2': 'Doctor of Osteopathy (DO)',
                '3': 'Certified Nurse Midwife (CNM)',
                '4': 'Other Midwife',
                '5': 'Other',
                '9': constants.UNKNOWN_NOT_STATED,
            }
        },
        'MTRAN': {
            'start': 434,
            'end': 434,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'PAY': {
            'start': 435,
            'end': 435,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Medicaid',
                '2': 'Private Insurance',
                '3': 'Self-Pay',
                '4': 'Indian Health Service',
                '5': 'CHAMPUS/TRICARE',
                '6': 'Other Government (Federal, State, Local)',
                '8': 'Other',
                '9': 'Unknown',
            }
        },
        'PAY_REC': {
            'start': 436,
            'end': 436,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Medicaid',
                '2': 'Private Insurance',
                '3': 'Self Pay',
                '4': 'Other',
                '9': 'Unknown',
            }
        },
        'F_PAY': {
            'start': 437,
            'end': 437,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_PAY_REC': {
            'start': 438,
            'end': 438,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'APGAR5': {
            'start': 444,
            'end': 445,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-10': 'A score of [value]',
                '99': constants.UNKNOWN_NOT_STATED
            }
        },
        'APGAR5R': {
            'start': 446,
            'end': 446,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'A score of 0-3',
                '2': 'A score of 4-6',
                '3': 'A score of 7-8',
                '4': 'A score of 9-10',
                '5': 'Unknown or not stated',
            }
        },
        'F_APGAR5': {
            'start': 447,
            'end': 447,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'APGAR10': {
            'start': 448,
            'end': 449,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '00-10': 'A score of [value]',
                '88': 'Not applicable',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'APGAR10R': {
            'start': 450,
            'end': 450,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'A score of 0-3',
                '2': 'A score of 4-6',
                '3': 'A score of 7-8',
                '4': 'A score of 9-10',
                '5': 'Not stated/not applicable',
            }
        },
        'DPLURAL': {
            'start': 454,
            'end': 454,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Single',
                '2': 'Twin',
                '3': 'Triplet',
                '4': 'Quadruplet',
                '5': 'Quintuplet or higher',
            }
        },
        'IMP_PLUR': {
            'start': 456,
            'end': 456,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Plurality is imputed',
                '1': 'Plurality is not imputed',
            }
        },
        'SETORDER_R': {
            'start': 459,
            'end': 459,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': '1st',
                '2': '2nd',
                '3': '3rd',
                '4': '4th',
                '5': '5th to 16th',
                '9': 'Unknown or not stated',
            }
        },
        'SEX': {
            'start': 475,
            'end': 475,
            'value': None,
            'definition': None,
            'valueDefinition': {
                'M': 'Male',
                'F': 'Female',
            }
        },
        'IMP_SEX': {
            'start': 476,
            'end': 476,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Infant Sex not Imputed',
                '1': 'Infant Sex is Imputed',
            }
        },
        'DLMP_MM': {
            'start': 477,
            'end': 478,
            'value': None,
            'definition': None,
            'valueDefinition': constants.MONTH
        },
        'DLMP_YY': {
            'start': 481,
            'end': 484,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '9999': constants.UNKNOWN_NOT_STATED,
                '*': 'Year [value] of last normal menses',
            }
        },
        'COMPGST_IMP': {
            'start': 488,
            'end': 488,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Combined Gestation is not imputed',
                '1': 'Combined Gestation is imputed',
            }
        },
        'OBGEST_FLG': {
            'start': 489,
            'end': 489,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Obstetric Estimate is not used',
                '1': 'Obstetric Estimate is used',
            }
        },
        'COMBGEST': {
            'start': 490,
            'end': 491,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '17-47': 'Week [value] of Gestation',
                '99': constants.UNKNOWN_NOT_STATED,
            }
        },
        'GESTREC10': {
            'start': 492,
            'end': 493,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': 'Under 20 weeks',
                '02': '20-27 weeks',
                '03': '28-31 weeks',
                '04': '32-33 weeks',
                '05': '34-36 weeks',
                '06': '37-38 weeks',
                '07': '39 weeks',
                '08': '40 weeks',
                '09': '41 weeks',
                '10': '42 weeks and over',
                '99': 'Unknown',
            }
        },
        'GESTREC3': {
            'start': 494,
            'end': 494,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Under 37 weeks',
                '2': '37 weeks and over',
                '3': 'Not stated',
            }
        },
        'LMPUSED': {
            'start': 498,
            'end': 498,
            'value': None,
            'definition': None,
            'valueDefinition': {
                ' ': 'Combined gestation not used',
                '1': 'Combined gestation used',
            }
        },
        'OEGest_Comb': {
            'start': 499,
            'end': 500,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '17-47': '[value] weeks of gestation',
                '99': 'Not stated',
            }
        },
        'OEGest_R10': {
            'start': 501,
            'end': 502,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': 'Under 20 weeks',
                '02': '20-27 weeks',
                '03': '28-31 weeks',
                '04': '32-33 weeks',
                '05': '34-36 weeks',
                '06': '37-38 weeks',
                '07': '39 weeks',
                '08': '40 weeks',
                '09': '41 weeks',
                '10': '42 weeks and over',
                '99': 'Unknown',
            }
        },
        'OEGest_R3': {
            'start': 503,
            'end': 503,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': 'Under 37 weeks',
                '2': '37 weeks and over',
                '3': 'Not stated',
            }
        },
        'DBWT': {
            'start': 504,
            'end': 507,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '0227-8165': '[value] grams',
                '9999': 'Not stated birth weigh',
            }
        },
        'BWTR12': {
            'start': 509,
            'end': 510,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '01': '0227 - 0499 grams',
                '02': '0500 - 0999 grams',
                '03': '1000 - 1499 grams',
                '04': '1500 - 1999 grams',
                '05': '2000 - 2499 grams',
                '06': '2500 - 2999 grams',
                '07': '3000 - 3499 grams',
                '08': '3500 - 3999 grams',
                '09': '4000 - 4499 grams',
                '10': '4500 - 4999 grams',
                '11': '5000 - 8165 grams',
                '12': 'Not Stated ',
            }
        },
        'BWTR4': {
            'start': 511,
            'end': 511,
            'value': None,
            'definition': None,
            'valueDefinition': {
                '1': '0227 - 1499 grams',
                '2': '1500 - 2499 grams',
                '3': '2500 - 8165 grams',
                '4': constants.UNKNOWN_NOT_STATED,
            }
        },
        'AB_AVEN1': {
            'start': 517,
            'end': 517,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_AVEN6': {
            'start': 518,
            'end': 518,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_NICU': {
            'start': 519,
            'end': 519,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_SURF': {
            'start': 520,
            'end': 520,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_ANTI': {
            'start': 521,
            'end': 521,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'AB_SEIZ': {
            'start': 522,
            'end': 522,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_AB_VENT': {
            'start': 524,
            'end': 524,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_VENT6': {
            'start': 525,
            'end': 525,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_NIUC': {
            'start': 526,
            'end': 526,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_SURFAC': {
            'start': 527,
            'end': 527,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_ANTIBIO': {
            'start': 528,
            'end': 528,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_AB_SEIZ': {
            'start': 529,
            'end': 529,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_ABNORM': {
            'start': 531,
            'end': 531,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'CA_ANEN': {
            'start': 537,
            'end': 537,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_MNSB': {
            'start': 538,
            'end': 538,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CCHD': {
            'start': 539,
            'end': 539,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CDH': {
            'start': 540,
            'end': 540,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_OMPH': {
            'start': 541,
            'end': 541,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_GAST': {
            'start': 542,
            'end': 542,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_CA_ANEN': {
            'start': 543,
            'end': 543,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_MENIN': {
            'start': 544,
            'end': 544,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_HEART': {
            'start': 545,
            'end': 545,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_HERNIA': {
            'start': 546,
            'end': 546,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_OMPHA': {
            'start': 547,
            'end': 547,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_GASTRO': {
            'start': 548,
            'end': 548,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'CA_LIMB': {
            'start': 549,
            'end': 549,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CLEFT': {
            'start': 550,
            'end': 550,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_CLPAL': {
            'start': 551,
            'end': 551,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_DOWN': {
            'start': 552,
            'end': 552,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'CA_DISOR': {
            'start': 553,
            'end': 553,
            'value': None,
            'definition': None,
            'valueDefinition': {
                'C': 'Confirmed',
                'P': 'Pending',
                'N': 'No',
                'U': 'Unknown',
            }
        },
        'CA_HYPO': {
            'start': 554,
            'end': 554,
            'value': None,
            'definition': None,
            'valueDefinition': {
                'Y': 'Yes, anomaly reported',
                'N': 'No, anomaly not reported',
                'U': 'Unknown',
            }
        },
        'F_CA_LIMB': {
            'start': 555,
            'end': 555,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_CLEFTLP': {
            'start': 556,
            'end': 556,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_CLEFT': {
            'start': 557,
            'end': 557,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_DOWNS': {
            'start': 558,
            'end': 558,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_CHROM': {
            'start': 559,
            'end': 559,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'F_CA_HYPOS': {
            'start': 560,
            'end': 560,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        },
        'NO_CONGEN': {
            'start': 561,
            'end': 561,
            'value': None,
            'definition': None,
            'valueDefinition': constants.TRUE_FALSE_NOT_REPORTED
        },
        'ITRAN': {
            'start': 567,
            'end': 567,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'ILIVE': {
            'start': 568,
            'end': 568,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'BFED': {
            'start': 569,
            'end': 569,
            'value': None,
            'definition': None,
            'valueDefinition': constants.YNU
        },
        'F_BFED': {
            'start': 570,
            'end': 570,
            'value': None,
            'definition': None,
            'valueDefinition': constants.REPORTING
        } 
    }
}