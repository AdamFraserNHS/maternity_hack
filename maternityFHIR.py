#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program reads the maternity wessex csv files and then creates a json file using the data retrieved based on the FHIR structure.
@author: af
"""

import numpy as np
import pandas as pd
import json as js
import csv as cv


## Define the paths


pathMaternity = 'maternity.csv'
pathJson = 'src/main/resources/maternity.json'


## Load and process (if required) the data using Pandas and the csv file.
## Provides a dataframe.


dfMaternity = pd.read_csv(pathMaternity)


def dem_dic_maternity_json(df):
    """
    This function uses dictionary to create the structure
    required for the Wessex maternity json file.

    Arguments:

        Input: df type - dataframe (pandas)
        Returns :  dict_json  - type dictionary.
    """

    dict_json = {}

    for i in range(len(df)):
        single_json = \
        {
            "resourceType": "Bundle",
            "id": "b96552fc-0e17-4535-90fa-236c32b04e2a",

            "type": "transaction",
            "entry": [
                {
                    "resource":
                    {
                        "fhir_comments": [
                            "Patient details"
                        ],
                        # The type of resource
                        "resourceType": "Patient",
                         #    "id": df.iloc[i]["patient_site_uid"],
                        "name" : [ {
                            "use": "official",
                            "text": df.iloc[i]["Full Name"],
                            "family": df.iloc[i]["Full Name"],
                            "given": [
                                df.iloc[i]["Full Name"]
                            ]
                        }],
                        "gender": "female",
                        # The gender of the individual: male | female | other | unknown
                        "birthDate": df.iloc[i]["Date of Birth"]
                    }
                },
                {
                      "fhir_comments": [
                          " Encounter resource entry - Admission by midwife"
                      ],
                      "resource": {
                          "resourceType": "Encounter",
                          "meta": {
                              "profile": [
                                  "https://fhir.hl7.org.uk/STU3/StructureDefinition/CareConnect-Encounter-1"
                              ]
                          },
                          "status": "finished",
                          "period": {
                              "start": df.iloc[i]["Maternity Start Date"]
                          },
                          "type":[ snomed_fhir("305323008", "Admission by midwife") ],
                      }
                },
                {
                      "fhir_comments": [
                          " Encounter resource entry - Birth"
                      ],
                      "resource": {
                          "resourceType": "Encounter",
                          "meta": {
                              "profile": [
                                  "https://fhir.nhs.uk/STU3/CodeSystem/DCH-ChildHealthEncounterType-1#003"
                              ]
                          },
                          "period": {
                              "start": df.iloc[i]["Actual delivery date"]
                          },
                          "location": [
                              { "location": [{
                                  "identifier": [
                                  {
                                      "system": "https://fhir.nhs.uk/Id/ods-site-code",
                                      "value": df.iloc[i]["Location of delivery"]
                                  }
                                  ],
                                  "display": df.iloc[i]["Location of delivery"]
                                }]
                              }
                          ]

                      }
                },
                fhir_observation("valueInteger", int(df.iloc[i]["Number of fetus (per conception)"]), "final",
                                            "382341000000101", "Total number of registerable births at delivery"),
                fhir_observation("valueInteger", int(df.iloc[i]["Number of fetus (per conception)"]),"final",
                                              "246435002", "Number of fetuses"),
                fhir_observation("valueDateTime",df.iloc[i]["Estimated Due Date"], "final",
                                              "161714006", "Estimated date of delivery"),
                fhir_observation("valueDateTime", df.iloc[i]["Estimated Due Date"], "preliminary",
                                 "289206005", "Estimated date of delivery from last period"),
                fhir_observation("valueDateTime", df.iloc[i]["Estimated Due Date"], "preliminary",
                                 "738070007", "Estimated date of delivery from antenatal ultrasound scan"),
            {
                "fhir_comments": [
                    "EpisodeOfCare resource"
                ],
                "resource": {
                    "resourceType": "EpisodeOfCare",
                    "meta": {
                        "profile": [
                            "https://fhir.hl7.org.uk/STU3/StructureDefinition/CareConnect-EpisodeOfCare-1"
                        ]
                    },
                    "type": [snomed_fhir("275305005", "Maternity care")],  # There is another episode of care preg/postnatal not sure !
                    "identifier": [
                        {
                            "system": "https://tools.ietf.org/html/rfc4122", # well this is definitely not correct !!
                            "value": df.iloc[i]["Pregnancy Identifier"]
                        }
                    ],
                    "status": "finished",
                    "patient": {
                        "reference": "urn:uuid:a4f0cbff-0c2b-414c-8696-9003fbc72c9e"
                    },
                    "period": {
                        "start": df.iloc[i]["Maternity Start Date"],
                        "end": df.iloc[i]["Maternity End Date"]
                    },
                    "statusHistory": [{
                        "period": {
                            "start": df.iloc[i]["Maternity Start Date"]
                        }
                    }],
                    "managingOrganization": {
                        "identifier":   [
                            {
                            "system": "https://fhir.nhs.uk/Id/ods-site-code",
                            "value": df.iloc[i]["Maternity services provider"]
                            } ]
                    }
                }
            },
            {
                "fhir_comments": [
                    "Referral request quite weak on knowledge here AF 2021-05-17 !"
                ],
                "resource": {
                    "resourceType": "ReferralRequest",
                    "meta": {
                        "profile": [
                            "https://fhir.nhs.uk/STU3/StructureDefinition/CareConnect-GPC-ReferralRequest-1"
                        ]
                    },
                    "authoredOn": df.iloc[i]["Maternity Start Date"],
                    "serviceRequested": [ snomed_fhir("424441002","Prenatal initial visit") ],
                    "description": "Referral for prenatal initial visit"
                }
            },
            {
                "fhir_comments": [
                    "Referral request quite weak on knowledge here AF 2021-05-17 !"
                ],
                "resource": {
                    "resourceType": "ReferralRequest",
                    "meta": {
                        "profile": [
                            "https://fhir.nhs.uk/STU3/StructureDefinition/CareConnect-GPC-ReferralRequest-1"
                        ]
                    },
                    "authoredOn": df.iloc[i]["Maternity Start Date"],
                    "recipient":   [{
                        "identifier":   [
                            {
                            "system": "https://fhir.nhs.uk/Id/ods-site-code",
                            "value": df.iloc[i]["Maternity services provider"]
                            } ]
                    }],
                    # , EpisodeOfCare.referralRequest := ReferralRequest  not sure...
                    "serviceRequested": [snomed_fhir("4563007", "Hospital admission, transfer from other hospital or health care facility")],
                    "description": "Referral for Hospital admission"
                }
            },
            {
                "resource": {
                    "resourceType": "CarePlan",
                    "meta": {
                        "profile": [
                            "https://fhir.nhs.uk/STU3/StructureDefinition/CareConnect-CarePlan-1"
                        ]
                    },
                    "author":[{
                        "identifier":   [
                            {
                            "system": "https://fhir.nhs.uk/Id/ods-site-code",
                            "value": df.iloc[i]["Maternity services provider"]
                            } ]
                         
                    }]
                }
            }
            ]
        }

        # dict_json.update({str(i): single_json})
        dict_json.update(single_json)
    return dict_json


def snomed_fhir(code, display=""):
    return {
        "coding": [
        {
            "system": "http://snomed.info/sct",
            "code": code,
            "display": display
        }
        ]
    }


def fhir_value(valueType, value):
    if (valueType== "valueDateTime"):
        return  {  "value": value,
                   "unit":"dateTime"}
    else:
        return  { "value": value,
                  "unit": "integer"}


def fhir_observation(valueType, value, status,snomed_code, snomed_display):
    json = {}

    dictReturn =  {
        "fhir_comments": [
            "Observation resource entry - " + snomed_display
        ],
        "resource": {
            "resourceType": "Observation",
            "meta": {
                "profile": [
                    "https://fhir.hl7.org.uk/STU3/StructureDefinition/CareConnect-Observation-1"
                ]
            },
            "status": status,
            "code": snomed_fhir(snomed_code, snomed_display)
        }
    }
    if valueType != "valueDateTime":
        json = {"valueQuantity": fhir_value(valueType, value)}
    else:
        json = {valueType: value}

    dictReturn["resource"].update(json)

    return dictReturn





dictJson = dem_dic_maternity_json(dfMaternity)

# ## Create the json file.
print(dfMaternity.iloc[0]["Discharge Date & Time"])


with open(pathJson, 'w') as demoFjson:
   js.dump(dictJson, demoFjson, indent=2)
