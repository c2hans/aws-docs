---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeSlot.html
---

# DescribeSlot
<a name="API_DescribeSlot"></a>

Gets metadata information about a slot.

## Request Syntax
<a name="API_DescribeSlot_RequestSyntax"></a>

```
GET /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/intents/{{intentId}}/slots/{{slotId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeSlot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DescribeSlot_RequestSyntax) **   <a name="lexv2-DescribeSlot-request-uri-botId"></a>
The identifier of the bot associated with the slot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_DescribeSlot_RequestSyntax) **   <a name="lexv2-DescribeSlot-request-uri-botVersion"></a>
The version of the bot associated with the slot.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [intentId](#API_DescribeSlot_RequestSyntax) **   <a name="lexv2-DescribeSlot-request-uri-intentId"></a>
The identifier of the intent that contains the slot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [localeId](#API_DescribeSlot_RequestSyntax) **   <a name="lexv2-DescribeSlot-request-uri-localeId"></a>
The identifier of the language and locale of the slot to describe. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

 ** [slotId](#API_DescribeSlot_RequestSyntax) **   <a name="lexv2-DescribeSlot-request-uri-slotId"></a>
The unique identifier for the slot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeSlot_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeSlot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "description": "string",
   "intentId": "string",
   "lastUpdatedDateTime": number,
   "localeId": "string",
   "multipleValuesSetting": {
      "allowMultipleValues": boolean
   },
   "obfuscationSetting": {
      "obfuscationSettingType": "string"
   },
   "slotId": "string",
   "slotName": "string",
   "slotTypeId": "string",
   "subSlotSetting": {
      "expression": "string",
      "slotSpecifications": {
         "string" : {
            "slotTypeId": "string",
            "valueElicitationSetting": {
               "defaultValueSpecification": {
                  "defaultValueList": [
                     {
                        "defaultValue": "string"
                     }
                  ]
               },
               "promptSpecification": {
                  "allowInterrupt": boolean,
                  "maxRetries": number,
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "string"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "string",
                                    "value": "string"
                                 }
                              ],
                              "imageUrl": "string",
                              "subtitle": "string",
                              "title": "string"
                           },
                           "plainTextMessage": {
                              "value": "string"
                           },
                           "ssmlMessage": {
                              "value": "string"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           }
                        ]
                     }
                  ],
                  "messageSelectionStrategy": "string",
                  "promptAttemptsSpecification": {
                     "string" : {
                        "allowedInputTypes": {
                           "allowAudioInput": boolean,
                           "allowDTMFInput": boolean
                        },
                        "allowInterrupt": boolean,
                        "audioAndDTMFInputSpecification": {
                           "audioSpecification": {
                              "endTimeoutMs": number,
                              "maxLengthMs": number
                           },
                           "dtmfSpecification": {
                              "deletionCharacter": "string",
                              "endCharacter": "string",
                              "endTimeoutMs": number,
                              "maxLength": number
                           },
                           "startTimeoutMs": number
                        },
                        "textInputSpecification": {
                           "startTimeoutMs": number
                        }
                     }
                  }
               },
               "sampleUtterances": [
                  {
                     "utterance": "string"
                  }
               ],
               "waitAndContinueSpecification": {
                  "active": boolean,
                  "continueResponse": {
                     "allowInterrupt": boolean,
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "string"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "string",
                                          "value": "string"
                                       }
                                    ],
                                    "imageUrl": "string",
                                    "subtitle": "string",
                                    "title": "string"
                                 },
                                 "plainTextMessage": {
                                    "value": "string"
                                 },
                                 "ssmlMessage": {
                                    "value": "string"
                                 }
                              }
                           ]
                        }
                     ]
                  },
                  "stillWaitingResponse": {
                     "allowInterrupt": boolean,
                     "frequencyInSeconds": number,
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "string"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "string",
                                          "value": "string"
                                       }
                                    ],
                                    "imageUrl": "string",
                                    "subtitle": "string",
                                    "title": "string"
                                 },
                                 "plainTextMessage": {
                                    "value": "string"
                                 },
                                 "ssmlMessage": {
                                    "value": "string"
                                 }
                              }
                           ]
                        }
                     ],
                     "timeoutInSeconds": number
                  },
                  "waitingResponse": {
                     "allowInterrupt": boolean,
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "string"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "string",
                                          "value": "string"
                                       }
                                    ],
                                    "imageUrl": "string",
                                    "subtitle": "string",
                                    "title": "string"
                                 },
                                 "plainTextMessage": {
                                    "value": "string"
                                 },
                                 "ssmlMessage": {
                                    "value": "string"
                                 }
                              }
                           ]
                        }
                     ]
                  }
               }
            }
         }
      }
   },
   "valueElicitationSetting": {
      "defaultValueSpecification": {
         "defaultValueList": [
            {
               "defaultValue": "string"
            }
         ]
      },
      "promptSpecification": {
         "allowInterrupt": boolean,
         "maxRetries": number,
         "messageGroups": [
            {
               "message": {
                  "customPayload": {
                     "value": "string"
                  },
                  "imageResponseCard": {
                     "buttons": [
                        {
                           "text": "string",
                           "value": "string"
                        }
                     ],
                     "imageUrl": "string",
                     "subtitle": "string",
                     "title": "string"
                  },
                  "plainTextMessage": {
                     "value": "string"
                  },
                  "ssmlMessage": {
                     "value": "string"
                  }
               },
               "variations": [
                  {
                     "customPayload": {
                        "value": "string"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "string",
                              "value": "string"
                           }
                        ],
                        "imageUrl": "string",
                        "subtitle": "string",
                        "title": "string"
                     },
                     "plainTextMessage": {
                        "value": "string"
                     },
                     "ssmlMessage": {
                        "value": "string"
                     }
                  }
               ]
            }
         ],
         "messageSelectionStrategy": "string",
         "promptAttemptsSpecification": {
            "string" : {
               "allowedInputTypes": {
                  "allowAudioInput": boolean,
                  "allowDTMFInput": boolean
               },
               "allowInterrupt": boolean,
               "audioAndDTMFInputSpecification": {
                  "audioSpecification": {
                     "endTimeoutMs": number,
                     "maxLengthMs": number
                  },
                  "dtmfSpecification": {
                     "deletionCharacter": "string",
                     "endCharacter": "string",
                     "endTimeoutMs": number,
                     "maxLength": number
                  },
                  "startTimeoutMs": number
               },
               "textInputSpecification": {
                  "startTimeoutMs": number
               }
            }
         }
      },
      "sampleUtterances": [
         {
            "utterance": "string"
         }
      ],
      "slotCaptureSetting": {
         "captureConditional": {
            "active": boolean,
            "conditionalBranches": [
               {
                  "condition": {
                     "expressionString": "string"
                  },
                  "name": "string",
                  "nextStep": {
                     "dialogAction": {
                        "slotToElicit": "string",
                        "suppressNextMessage": boolean,
                        "type": "string"
                     },
                     "intent": {
                        "name": "string",
                        "slots": {
                           "string" : {
                              "shape": "string",
                              "value": {
                                 "interpretedValue": "string"
                              },
                              "values": [
                                 "SlotValueOverride"
                              ]
                           }
                        }
                     },
                     "sessionAttributes": {
                        "string" : "string"
                     }
                  },
                  "response": {
                     "allowInterrupt": boolean,
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "string"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "string",
                                          "value": "string"
                                       }
                                    ],
                                    "imageUrl": "string",
                                    "subtitle": "string",
                                    "title": "string"
                                 },
                                 "plainTextMessage": {
                                    "value": "string"
                                 },
                                 "ssmlMessage": {
                                    "value": "string"
                                 }
                              }
                           ]
                        }
                     ]
                  }
               }
            ],
            "defaultBranch": {
               "nextStep": {
                  "dialogAction": {
                     "slotToElicit": "string",
                     "suppressNextMessage": boolean,
                     "type": "string"
                  },
                  "intent": {
                     "name": "string",
                     "slots": {
                        "string" : {
                           "shape": "string",
                           "value": {
                              "interpretedValue": "string"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "string" : "string"
                  }
               },
               "response": {
                  "allowInterrupt": boolean,
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "string"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "string",
                                    "value": "string"
                                 }
                              ],
                              "imageUrl": "string",
                              "subtitle": "string",
                              "title": "string"
                           },
                           "plainTextMessage": {
                              "value": "string"
                           },
                           "ssmlMessage": {
                              "value": "string"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           }
                        ]
                     }
                  ]
               }
            }
         },
         "captureNextStep": {
            "dialogAction": {
               "slotToElicit": "string",
               "suppressNextMessage": boolean,
               "type": "string"
            },
            "intent": {
               "name": "string",
               "slots": {
                  "string" : {
                     "shape": "string",
                     "value": {
                        "interpretedValue": "string"
                     },
                     "values": [
                        "SlotValueOverride"
                     ]
                  }
               }
            },
            "sessionAttributes": {
               "string" : "string"
            }
         },
         "captureResponse": {
            "allowInterrupt": boolean,
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "string"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "string",
                              "value": "string"
                           }
                        ],
                        "imageUrl": "string",
                        "subtitle": "string",
                        "title": "string"
                     },
                     "plainTextMessage": {
                        "value": "string"
                     },
                     "ssmlMessage": {
                        "value": "string"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "string"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "string",
                                 "value": "string"
                              }
                           ],
                           "imageUrl": "string",
                           "subtitle": "string",
                           "title": "string"
                        },
                        "plainTextMessage": {
                           "value": "string"
                        },
                        "ssmlMessage": {
                           "value": "string"
                        }
                     }
                  ]
               }
            ]
         },
         "codeHook": {
            "active": boolean,
            "enableCodeHookInvocation": boolean,
            "invocationLabel": "string",
            "postCodeHookSpecification": {
               "failureConditional": {
                  "active": boolean,
                  "conditionalBranches": [
                     {
                        "condition": {
                           "expressionString": "string"
                        },
                        "name": "string",
                        "nextStep": {
                           "dialogAction": {
                              "slotToElicit": "string",
                              "suppressNextMessage": boolean,
                              "type": "string"
                           },
                           "intent": {
                              "name": "string",
                              "slots": {
                                 "string" : {
                                    "shape": "string",
                                    "value": {
                                       "interpretedValue": "string"
                                    },
                                    "values": [
                                       "SlotValueOverride"
                                    ]
                                 }
                              }
                           },
                           "sessionAttributes": {
                              "string" : "string"
                           }
                        },
                        "response": {
                           "allowInterrupt": boolean,
                           "messageGroups": [
                              {
                                 "message": {
                                    "customPayload": {
                                       "value": "string"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "string",
                                             "value": "string"
                                          }
                                       ],
                                       "imageUrl": "string",
                                       "subtitle": "string",
                                       "title": "string"
                                    },
                                    "plainTextMessage": {
                                       "value": "string"
                                    },
                                    "ssmlMessage": {
                                       "value": "string"
                                    }
                                 },
                                 "variations": [
                                    {
                                       "customPayload": {
                                          "value": "string"
                                       },
                                       "imageResponseCard": {
                                          "buttons": [
                                             {
                                                "text": "string",
                                                "value": "string"
                                             }
                                          ],
                                          "imageUrl": "string",
                                          "subtitle": "string",
                                          "title": "string"
                                       },
                                       "plainTextMessage": {
                                          "value": "string"
                                       },
                                       "ssmlMessage": {
                                          "value": "string"
                                       }
                                    }
                                 ]
                              }
                           ]
                        }
                     }
                  ],
                  "defaultBranch": {
                     "nextStep": {
                        "dialogAction": {
                           "slotToElicit": "string",
                           "suppressNextMessage": boolean,
                           "type": "string"
                        },
                        "intent": {
                           "name": "string",
                           "slots": {
                              "string" : {
                                 "shape": "string",
                                 "value": {
                                    "interpretedValue": "string"
                                 },
                                 "values": [
                                    "SlotValueOverride"
                                 ]
                              }
                           }
                        },
                        "sessionAttributes": {
                           "string" : "string"
                        }
                     },
                     "response": {
                        "allowInterrupt": boolean,
                        "messageGroups": [
                           {
                              "message": {
                                 "customPayload": {
                                    "value": "string"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "string",
                                          "value": "string"
                                       }
                                    ],
                                    "imageUrl": "string",
                                    "subtitle": "string",
                                    "title": "string"
                                 },
                                 "plainTextMessage": {
                                    "value": "string"
                                 },
                                 "ssmlMessage": {
                                    "value": "string"
                                 }
                              },
                              "variations": [
                                 {
                                    "customPayload": {
                                       "value": "string"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "string",
                                             "value": "string"
                                          }
                                       ],
                                       "imageUrl": "string",
                                       "subtitle": "string",
                                       "title": "string"
                                    },
                                    "plainTextMessage": {
                                       "value": "string"
                                    },
                                    "ssmlMessage": {
                                       "value": "string"
                                    }
                                 }
                              ]
                           }
                        ]
                     }
                  }
               },
               "failureNextStep": {
                  "dialogAction": {
                     "slotToElicit": "string",
                     "suppressNextMessage": boolean,
                     "type": "string"
                  },
                  "intent": {
                     "name": "string",
                     "slots": {
                        "string" : {
                           "shape": "string",
                           "value": {
                              "interpretedValue": "string"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "string" : "string"
                  }
               },
               "failureResponse": {
                  "allowInterrupt": boolean,
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "string"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "string",
                                    "value": "string"
                                 }
                              ],
                              "imageUrl": "string",
                              "subtitle": "string",
                              "title": "string"
                           },
                           "plainTextMessage": {
                              "value": "string"
                           },
                           "ssmlMessage": {
                              "value": "string"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           }
                        ]
                     }
                  ]
               },
               "successConditional": {
                  "active": boolean,
                  "conditionalBranches": [
                     {
                        "condition": {
                           "expressionString": "string"
                        },
                        "name": "string",
                        "nextStep": {
                           "dialogAction": {
                              "slotToElicit": "string",
                              "suppressNextMessage": boolean,
                              "type": "string"
                           },
                           "intent": {
                              "name": "string",
                              "slots": {
                                 "string" : {
                                    "shape": "string",
                                    "value": {
                                       "interpretedValue": "string"
                                    },
                                    "values": [
                                       "SlotValueOverride"
                                    ]
                                 }
                              }
                           },
                           "sessionAttributes": {
                              "string" : "string"
                           }
                        },
                        "response": {
                           "allowInterrupt": boolean,
                           "messageGroups": [
                              {
                                 "message": {
                                    "customPayload": {
                                       "value": "string"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "string",
                                             "value": "string"
                                          }
                                       ],
                                       "imageUrl": "string",
                                       "subtitle": "string",
                                       "title": "string"
                                    },
                                    "plainTextMessage": {
                                       "value": "string"
                                    },
                                    "ssmlMessage": {
                                       "value": "string"
                                    }
                                 },
                                 "variations": [
                                    {
                                       "customPayload": {
                                          "value": "string"
                                       },
                                       "imageResponseCard": {
                                          "buttons": [
                                             {
                                                "text": "string",
                                                "value": "string"
                                             }
                                          ],
                                          "imageUrl": "string",
                                          "subtitle": "string",
                                          "title": "string"
                                       },
                                       "plainTextMessage": {
                                          "value": "string"
                                       },
                                       "ssmlMessage": {
                                          "value": "string"
                                       }
                                    }
                                 ]
                              }
                           ]
                        }
                     }
                  ],
                  "defaultBranch": {
                     "nextStep": {
                        "dialogAction": {
                           "slotToElicit": "string",
                           "suppressNextMessage": boolean,
                           "type": "string"
                        },
                        "intent": {
                           "name": "string",
                           "slots": {
                              "string" : {
                                 "shape": "string",
                                 "value": {
                                    "interpretedValue": "string"
                                 },
                                 "values": [
                                    "SlotValueOverride"
                                 ]
                              }
                           }
                        },
                        "sessionAttributes": {
                           "string" : "string"
                        }
                     },
                     "response": {
                        "allowInterrupt": boolean,
                        "messageGroups": [
                           {
                              "message": {
                                 "customPayload": {
                                    "value": "string"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "string",
                                          "value": "string"
                                       }
                                    ],
                                    "imageUrl": "string",
                                    "subtitle": "string",
                                    "title": "string"
                                 },
                                 "plainTextMessage": {
                                    "value": "string"
                                 },
                                 "ssmlMessage": {
                                    "value": "string"
                                 }
                              },
                              "variations": [
                                 {
                                    "customPayload": {
                                       "value": "string"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "string",
                                             "value": "string"
                                          }
                                       ],
                                       "imageUrl": "string",
                                       "subtitle": "string",
                                       "title": "string"
                                    },
                                    "plainTextMessage": {
                                       "value": "string"
                                    },
                                    "ssmlMessage": {
                                       "value": "string"
                                    }
                                 }
                              ]
                           }
                        ]
                     }
                  }
               },
               "successNextStep": {
                  "dialogAction": {
                     "slotToElicit": "string",
                     "suppressNextMessage": boolean,
                     "type": "string"
                  },
                  "intent": {
                     "name": "string",
                     "slots": {
                        "string" : {
                           "shape": "string",
                           "value": {
                              "interpretedValue": "string"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "string" : "string"
                  }
               },
               "successResponse": {
                  "allowInterrupt": boolean,
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "string"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "string",
                                    "value": "string"
                                 }
                              ],
                              "imageUrl": "string",
                              "subtitle": "string",
                              "title": "string"
                           },
                           "plainTextMessage": {
                              "value": "string"
                           },
                           "ssmlMessage": {
                              "value": "string"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           }
                        ]
                     }
                  ]
               },
               "timeoutConditional": {
                  "active": boolean,
                  "conditionalBranches": [
                     {
                        "condition": {
                           "expressionString": "string"
                        },
                        "name": "string",
                        "nextStep": {
                           "dialogAction": {
                              "slotToElicit": "string",
                              "suppressNextMessage": boolean,
                              "type": "string"
                           },
                           "intent": {
                              "name": "string",
                              "slots": {
                                 "string" : {
                                    "shape": "string",
                                    "value": {
                                       "interpretedValue": "string"
                                    },
                                    "values": [
                                       "SlotValueOverride"
                                    ]
                                 }
                              }
                           },
                           "sessionAttributes": {
                              "string" : "string"
                           }
                        },
                        "response": {
                           "allowInterrupt": boolean,
                           "messageGroups": [
                              {
                                 "message": {
                                    "customPayload": {
                                       "value": "string"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "string",
                                             "value": "string"
                                          }
                                       ],
                                       "imageUrl": "string",
                                       "subtitle": "string",
                                       "title": "string"
                                    },
                                    "plainTextMessage": {
                                       "value": "string"
                                    },
                                    "ssmlMessage": {
                                       "value": "string"
                                    }
                                 },
                                 "variations": [
                                    {
                                       "customPayload": {
                                          "value": "string"
                                       },
                                       "imageResponseCard": {
                                          "buttons": [
                                             {
                                                "text": "string",
                                                "value": "string"
                                             }
                                          ],
                                          "imageUrl": "string",
                                          "subtitle": "string",
                                          "title": "string"
                                       },
                                       "plainTextMessage": {
                                          "value": "string"
                                       },
                                       "ssmlMessage": {
                                          "value": "string"
                                       }
                                    }
                                 ]
                              }
                           ]
                        }
                     }
                  ],
                  "defaultBranch": {
                     "nextStep": {
                        "dialogAction": {
                           "slotToElicit": "string",
                           "suppressNextMessage": boolean,
                           "type": "string"
                        },
                        "intent": {
                           "name": "string",
                           "slots": {
                              "string" : {
                                 "shape": "string",
                                 "value": {
                                    "interpretedValue": "string"
                                 },
                                 "values": [
                                    "SlotValueOverride"
                                 ]
                              }
                           }
                        },
                        "sessionAttributes": {
                           "string" : "string"
                        }
                     },
                     "response": {
                        "allowInterrupt": boolean,
                        "messageGroups": [
                           {
                              "message": {
                                 "customPayload": {
                                    "value": "string"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "string",
                                          "value": "string"
                                       }
                                    ],
                                    "imageUrl": "string",
                                    "subtitle": "string",
                                    "title": "string"
                                 },
                                 "plainTextMessage": {
                                    "value": "string"
                                 },
                                 "ssmlMessage": {
                                    "value": "string"
                                 }
                              },
                              "variations": [
                                 {
                                    "customPayload": {
                                       "value": "string"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "string",
                                             "value": "string"
                                          }
                                       ],
                                       "imageUrl": "string",
                                       "subtitle": "string",
                                       "title": "string"
                                    },
                                    "plainTextMessage": {
                                       "value": "string"
                                    },
                                    "ssmlMessage": {
                                       "value": "string"
                                    }
                                 }
                              ]
                           }
                        ]
                     }
                  }
               },
               "timeoutNextStep": {
                  "dialogAction": {
                     "slotToElicit": "string",
                     "suppressNextMessage": boolean,
                     "type": "string"
                  },
                  "intent": {
                     "name": "string",
                     "slots": {
                        "string" : {
                           "shape": "string",
                           "value": {
                              "interpretedValue": "string"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "string" : "string"
                  }
               },
               "timeoutResponse": {
                  "allowInterrupt": boolean,
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "string"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "string",
                                    "value": "string"
                                 }
                              ],
                              "imageUrl": "string",
                              "subtitle": "string",
                              "title": "string"
                           },
                           "plainTextMessage": {
                              "value": "string"
                           },
                           "ssmlMessage": {
                              "value": "string"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           }
                        ]
                     }
                  ]
               }
            }
         },
         "elicitationCodeHook": {
            "enableCodeHookInvocation": boolean,
            "invocationLabel": "string"
         },
         "failureConditional": {
            "active": boolean,
            "conditionalBranches": [
               {
                  "condition": {
                     "expressionString": "string"
                  },
                  "name": "string",
                  "nextStep": {
                     "dialogAction": {
                        "slotToElicit": "string",
                        "suppressNextMessage": boolean,
                        "type": "string"
                     },
                     "intent": {
                        "name": "string",
                        "slots": {
                           "string" : {
                              "shape": "string",
                              "value": {
                                 "interpretedValue": "string"
                              },
                              "values": [
                                 "SlotValueOverride"
                              ]
                           }
                        }
                     },
                     "sessionAttributes": {
                        "string" : "string"
                     }
                  },
                  "response": {
                     "allowInterrupt": boolean,
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "string"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "string",
                                          "value": "string"
                                       }
                                    ],
                                    "imageUrl": "string",
                                    "subtitle": "string",
                                    "title": "string"
                                 },
                                 "plainTextMessage": {
                                    "value": "string"
                                 },
                                 "ssmlMessage": {
                                    "value": "string"
                                 }
                              }
                           ]
                        }
                     ]
                  }
               }
            ],
            "defaultBranch": {
               "nextStep": {
                  "dialogAction": {
                     "slotToElicit": "string",
                     "suppressNextMessage": boolean,
                     "type": "string"
                  },
                  "intent": {
                     "name": "string",
                     "slots": {
                        "string" : {
                           "shape": "string",
                           "value": {
                              "interpretedValue": "string"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "string" : "string"
                  }
               },
               "response": {
                  "allowInterrupt": boolean,
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "string"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "string",
                                    "value": "string"
                                 }
                              ],
                              "imageUrl": "string",
                              "subtitle": "string",
                              "title": "string"
                           },
                           "plainTextMessage": {
                              "value": "string"
                           },
                           "ssmlMessage": {
                              "value": "string"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "string"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "string",
                                       "value": "string"
                                    }
                                 ],
                                 "imageUrl": "string",
                                 "subtitle": "string",
                                 "title": "string"
                              },
                              "plainTextMessage": {
                                 "value": "string"
                              },
                              "ssmlMessage": {
                                 "value": "string"
                              }
                           }
                        ]
                     }
                  ]
               }
            }
         },
         "failureNextStep": {
            "dialogAction": {
               "slotToElicit": "string",
               "suppressNextMessage": boolean,
               "type": "string"
            },
            "intent": {
               "name": "string",
               "slots": {
                  "string" : {
                     "shape": "string",
                     "value": {
                        "interpretedValue": "string"
                     },
                     "values": [
                        "SlotValueOverride"
                     ]
                  }
               }
            },
            "sessionAttributes": {
               "string" : "string"
            }
         },
         "failureResponse": {
            "allowInterrupt": boolean,
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "string"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "string",
                              "value": "string"
                           }
                        ],
                        "imageUrl": "string",
                        "subtitle": "string",
                        "title": "string"
                     },
                     "plainTextMessage": {
                        "value": "string"
                     },
                     "ssmlMessage": {
                        "value": "string"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "string"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "string",
                                 "value": "string"
                              }
                           ],
                           "imageUrl": "string",
                           "subtitle": "string",
                           "title": "string"
                        },
                        "plainTextMessage": {
                           "value": "string"
                        },
                        "ssmlMessage": {
                           "value": "string"
                        }
                     }
                  ]
               }
            ]
         }
      },
      "slotConstraint": "string",
      "slotResolutionSetting": {
         "slotResolutionStrategy": "string"
      },
      "waitAndContinueSpecification": {
         "active": boolean,
         "continueResponse": {
            "allowInterrupt": boolean,
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "string"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "string",
                              "value": "string"
                           }
                        ],
                        "imageUrl": "string",
                        "subtitle": "string",
                        "title": "string"
                     },
                     "plainTextMessage": {
                        "value": "string"
                     },
                     "ssmlMessage": {
                        "value": "string"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "string"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "string",
                                 "value": "string"
                              }
                           ],
                           "imageUrl": "string",
                           "subtitle": "string",
                           "title": "string"
                        },
                        "plainTextMessage": {
                           "value": "string"
                        },
                        "ssmlMessage": {
                           "value": "string"
                        }
                     }
                  ]
               }
            ]
         },
         "stillWaitingResponse": {
            "allowInterrupt": boolean,
            "frequencyInSeconds": number,
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "string"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "string",
                              "value": "string"
                           }
                        ],
                        "imageUrl": "string",
                        "subtitle": "string",
                        "title": "string"
                     },
                     "plainTextMessage": {
                        "value": "string"
                     },
                     "ssmlMessage": {
                        "value": "string"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "string"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "string",
                                 "value": "string"
                              }
                           ],
                           "imageUrl": "string",
                           "subtitle": "string",
                           "title": "string"
                        },
                        "plainTextMessage": {
                           "value": "string"
                        },
                        "ssmlMessage": {
                           "value": "string"
                        }
                     }
                  ]
               }
            ],
            "timeoutInSeconds": number
         },
         "waitingResponse": {
            "allowInterrupt": boolean,
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "string"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "string",
                              "value": "string"
                           }
                        ],
                        "imageUrl": "string",
                        "subtitle": "string",
                        "title": "string"
                     },
                     "plainTextMessage": {
                        "value": "string"
                     },
                     "ssmlMessage": {
                        "value": "string"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "string"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "string",
                                 "value": "string"
                              }
                           ],
                           "imageUrl": "string",
                           "subtitle": "string",
                           "title": "string"
                        },
                        "plainTextMessage": {
                           "value": "string"
                        },
                        "ssmlMessage": {
                           "value": "string"
                        }
                     }
                  ]
               }
            ]
         }
      }
   }
}
```

## Response Elements
<a name="API_DescribeSlot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-botId"></a>
The identifier of the bot associated with the slot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-botVersion"></a>
The version of the bot associated with the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`

 ** [creationDateTime](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-creationDateTime"></a>
A timestamp of the date and time that the slot was created.
Type: Timestamp

 ** [description](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-description"></a>
The description specified for the slot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [intentId](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-intentId"></a>
The identifier of the intent associated with the slot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [lastUpdatedDateTime](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-lastUpdatedDateTime"></a>
A timestamp of the date and time that the slot was last updated.
Type: Timestamp

 ** [localeId](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-localeId"></a>
The language and locale specified for the slot.
Type: String

 ** [multipleValuesSetting](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-multipleValuesSetting"></a>
Indicates whether the slot accepts multiple values in a single utterance.
If the `multipleValuesSetting` is not set, the default value is `false`.
Type: [MultipleValuesSetting](API_MultipleValuesSetting.md) object

 ** [obfuscationSetting](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-obfuscationSetting"></a>
Whether slot values are shown in Amazon CloudWatch logs. If the value is `None`, the actual value of the slot is shown in logs.
Type: [ObfuscationSetting](API_ObfuscationSetting.md) object

 ** [slotId](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-slotId"></a>
The unique identifier generated for the slot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [slotName](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-slotName"></a>
The name specified for the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [slotTypeId](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-slotTypeId"></a>
The identifier of the slot type that determines the values entered into the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`

 ** [subSlotSetting](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-subSlotSetting"></a>
Specifications for the constituent sub slots and the expression for the composite slot.
Type: [SubSlotSetting](API_SubSlotSetting.md) object

 ** [valueElicitationSetting](#API_DescribeSlot_ResponseSyntax) **   <a name="lexv2-DescribeSlot-response-valueElicitationSetting"></a>
Prompts that Amazon Lex uses to elicit a value for the slot.
Type: [SlotValueElicitationSetting](API_SlotValueElicitationSetting.md) object

## Errors
<a name="API_DescribeSlot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSlot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeSlot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeSlot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeSlot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeSlot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeSlot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeSlot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeSlot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeSlot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeSlot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeSlot)
