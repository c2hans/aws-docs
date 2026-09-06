---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateSlot.html
---

# CreateSlot
<a name="API_CreateSlot"></a>

Creates a slot in an intent. A slot is a variable needed to fulfill an intent. For example, an `OrderPizza` intent might need slots for size, crust, and number of pizzas. For each slot, you define one or more utterances that Amazon Lex uses to elicit a response from the user.

## Request Syntax
<a name="API_CreateSlot_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/intents/{{intentId}}/slots/ HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "multipleValuesSetting": {
      "allowMultipleValues": {{boolean}}
   },
   "obfuscationSetting": {
      "obfuscationSettingType": "{{string}}"
   },
   "slotName": "{{string}}",
   "slotTypeId": "{{string}}",
   "subSlotSetting": {
      "expression": "{{string}}",
      "slotSpecifications": {
         "{{string}}" : {
            "slotTypeId": "{{string}}",
            "valueElicitationSetting": {
               "defaultValueSpecification": {
                  "defaultValueList": [
                     {
                        "defaultValue": "{{string}}"
                     }
                  ]
               },
               "promptSpecification": {
                  "allowInterrupt": {{boolean}},
                  "maxRetries": {{number}},
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "{{string}}"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "{{string}}",
                                    "value": "{{string}}"
                                 }
                              ],
                              "imageUrl": "{{string}}",
                              "subtitle": "{{string}}",
                              "title": "{{string}}"
                           },
                           "plainTextMessage": {
                              "value": "{{string}}"
                           },
                           "ssmlMessage": {
                              "value": "{{string}}"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
                              }
                           }
                        ]
                     }
                  ],
                  "messageSelectionStrategy": "{{string}}",
                  "promptAttemptsSpecification": {
                     "{{string}}" : {
                        "allowedInputTypes": {
                           "allowAudioInput": {{boolean}},
                           "allowDTMFInput": {{boolean}}
                        },
                        "allowInterrupt": {{boolean}},
                        "audioAndDTMFInputSpecification": {
                           "audioSpecification": {
                              "endTimeoutMs": {{number}},
                              "maxLengthMs": {{number}}
                           },
                           "dtmfSpecification": {
                              "deletionCharacter": "{{string}}",
                              "endCharacter": "{{string}}",
                              "endTimeoutMs": {{number}},
                              "maxLength": {{number}}
                           },
                           "startTimeoutMs": {{number}}
                        },
                        "textInputSpecification": {
                           "startTimeoutMs": {{number}}
                        }
                     }
                  }
               },
               "sampleUtterances": [
                  {
                     "utterance": "{{string}}"
                  }
               ],
               "waitAndContinueSpecification": {
                  "active": {{boolean}},
                  "continueResponse": {
                     "allowInterrupt": {{boolean}},
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "{{string}}"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "{{string}}",
                                          "value": "{{string}}"
                                       }
                                    ],
                                    "imageUrl": "{{string}}",
                                    "subtitle": "{{string}}",
                                    "title": "{{string}}"
                                 },
                                 "plainTextMessage": {
                                    "value": "{{string}}"
                                 },
                                 "ssmlMessage": {
                                    "value": "{{string}}"
                                 }
                              }
                           ]
                        }
                     ]
                  },
                  "stillWaitingResponse": {
                     "allowInterrupt": {{boolean}},
                     "frequencyInSeconds": {{number}},
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "{{string}}"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "{{string}}",
                                          "value": "{{string}}"
                                       }
                                    ],
                                    "imageUrl": "{{string}}",
                                    "subtitle": "{{string}}",
                                    "title": "{{string}}"
                                 },
                                 "plainTextMessage": {
                                    "value": "{{string}}"
                                 },
                                 "ssmlMessage": {
                                    "value": "{{string}}"
                                 }
                              }
                           ]
                        }
                     ],
                     "timeoutInSeconds": {{number}}
                  },
                  "waitingResponse": {
                     "allowInterrupt": {{boolean}},
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "{{string}}"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "{{string}}",
                                          "value": "{{string}}"
                                       }
                                    ],
                                    "imageUrl": "{{string}}",
                                    "subtitle": "{{string}}",
                                    "title": "{{string}}"
                                 },
                                 "plainTextMessage": {
                                    "value": "{{string}}"
                                 },
                                 "ssmlMessage": {
                                    "value": "{{string}}"
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
               "defaultValue": "{{string}}"
            }
         ]
      },
      "promptSpecification": {
         "allowInterrupt": {{boolean}},
         "maxRetries": {{number}},
         "messageGroups": [
            {
               "message": {
                  "customPayload": {
                     "value": "{{string}}"
                  },
                  "imageResponseCard": {
                     "buttons": [
                        {
                           "text": "{{string}}",
                           "value": "{{string}}"
                        }
                     ],
                     "imageUrl": "{{string}}",
                     "subtitle": "{{string}}",
                     "title": "{{string}}"
                  },
                  "plainTextMessage": {
                     "value": "{{string}}"
                  },
                  "ssmlMessage": {
                     "value": "{{string}}"
                  }
               },
               "variations": [
                  {
                     "customPayload": {
                        "value": "{{string}}"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "{{string}}",
                              "value": "{{string}}"
                           }
                        ],
                        "imageUrl": "{{string}}",
                        "subtitle": "{{string}}",
                        "title": "{{string}}"
                     },
                     "plainTextMessage": {
                        "value": "{{string}}"
                     },
                     "ssmlMessage": {
                        "value": "{{string}}"
                     }
                  }
               ]
            }
         ],
         "messageSelectionStrategy": "{{string}}",
         "promptAttemptsSpecification": {
            "{{string}}" : {
               "allowedInputTypes": {
                  "allowAudioInput": {{boolean}},
                  "allowDTMFInput": {{boolean}}
               },
               "allowInterrupt": {{boolean}},
               "audioAndDTMFInputSpecification": {
                  "audioSpecification": {
                     "endTimeoutMs": {{number}},
                     "maxLengthMs": {{number}}
                  },
                  "dtmfSpecification": {
                     "deletionCharacter": "{{string}}",
                     "endCharacter": "{{string}}",
                     "endTimeoutMs": {{number}},
                     "maxLength": {{number}}
                  },
                  "startTimeoutMs": {{number}}
               },
               "textInputSpecification": {
                  "startTimeoutMs": {{number}}
               }
            }
         }
      },
      "sampleUtterances": [
         {
            "utterance": "{{string}}"
         }
      ],
      "slotCaptureSetting": {
         "captureConditional": {
            "active": {{boolean}},
            "conditionalBranches": [
               {
                  "condition": {
                     "expressionString": "{{string}}"
                  },
                  "name": "{{string}}",
                  "nextStep": {
                     "dialogAction": {
                        "slotToElicit": "{{string}}",
                        "suppressNextMessage": {{boolean}},
                        "type": "{{string}}"
                     },
                     "intent": {
                        "name": "{{string}}",
                        "slots": {
                           "{{string}}" : {
                              "shape": "{{string}}",
                              "value": {
                                 "interpretedValue": "{{string}}"
                              },
                              "values": [
                                 "SlotValueOverride"
                              ]
                           }
                        }
                     },
                     "sessionAttributes": {
                        "{{string}}" : "{{string}}"
                     }
                  },
                  "response": {
                     "allowInterrupt": {{boolean}},
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "{{string}}"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "{{string}}",
                                          "value": "{{string}}"
                                       }
                                    ],
                                    "imageUrl": "{{string}}",
                                    "subtitle": "{{string}}",
                                    "title": "{{string}}"
                                 },
                                 "plainTextMessage": {
                                    "value": "{{string}}"
                                 },
                                 "ssmlMessage": {
                                    "value": "{{string}}"
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
                     "slotToElicit": "{{string}}",
                     "suppressNextMessage": {{boolean}},
                     "type": "{{string}}"
                  },
                  "intent": {
                     "name": "{{string}}",
                     "slots": {
                        "{{string}}" : {
                           "shape": "{{string}}",
                           "value": {
                              "interpretedValue": "{{string}}"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "{{string}}" : "{{string}}"
                  }
               },
               "response": {
                  "allowInterrupt": {{boolean}},
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "{{string}}"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "{{string}}",
                                    "value": "{{string}}"
                                 }
                              ],
                              "imageUrl": "{{string}}",
                              "subtitle": "{{string}}",
                              "title": "{{string}}"
                           },
                           "plainTextMessage": {
                              "value": "{{string}}"
                           },
                           "ssmlMessage": {
                              "value": "{{string}}"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
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
               "slotToElicit": "{{string}}",
               "suppressNextMessage": {{boolean}},
               "type": "{{string}}"
            },
            "intent": {
               "name": "{{string}}",
               "slots": {
                  "{{string}}" : {
                     "shape": "{{string}}",
                     "value": {
                        "interpretedValue": "{{string}}"
                     },
                     "values": [
                        "SlotValueOverride"
                     ]
                  }
               }
            },
            "sessionAttributes": {
               "{{string}}" : "{{string}}"
            }
         },
         "captureResponse": {
            "allowInterrupt": {{boolean}},
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "{{string}}"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "{{string}}",
                              "value": "{{string}}"
                           }
                        ],
                        "imageUrl": "{{string}}",
                        "subtitle": "{{string}}",
                        "title": "{{string}}"
                     },
                     "plainTextMessage": {
                        "value": "{{string}}"
                     },
                     "ssmlMessage": {
                        "value": "{{string}}"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "{{string}}"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "{{string}}",
                                 "value": "{{string}}"
                              }
                           ],
                           "imageUrl": "{{string}}",
                           "subtitle": "{{string}}",
                           "title": "{{string}}"
                        },
                        "plainTextMessage": {
                           "value": "{{string}}"
                        },
                        "ssmlMessage": {
                           "value": "{{string}}"
                        }
                     }
                  ]
               }
            ]
         },
         "codeHook": {
            "active": {{boolean}},
            "enableCodeHookInvocation": {{boolean}},
            "invocationLabel": "{{string}}",
            "postCodeHookSpecification": {
               "failureConditional": {
                  "active": {{boolean}},
                  "conditionalBranches": [
                     {
                        "condition": {
                           "expressionString": "{{string}}"
                        },
                        "name": "{{string}}",
                        "nextStep": {
                           "dialogAction": {
                              "slotToElicit": "{{string}}",
                              "suppressNextMessage": {{boolean}},
                              "type": "{{string}}"
                           },
                           "intent": {
                              "name": "{{string}}",
                              "slots": {
                                 "{{string}}" : {
                                    "shape": "{{string}}",
                                    "value": {
                                       "interpretedValue": "{{string}}"
                                    },
                                    "values": [
                                       "SlotValueOverride"
                                    ]
                                 }
                              }
                           },
                           "sessionAttributes": {
                              "{{string}}" : "{{string}}"
                           }
                        },
                        "response": {
                           "allowInterrupt": {{boolean}},
                           "messageGroups": [
                              {
                                 "message": {
                                    "customPayload": {
                                       "value": "{{string}}"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "{{string}}",
                                             "value": "{{string}}"
                                          }
                                       ],
                                       "imageUrl": "{{string}}",
                                       "subtitle": "{{string}}",
                                       "title": "{{string}}"
                                    },
                                    "plainTextMessage": {
                                       "value": "{{string}}"
                                    },
                                    "ssmlMessage": {
                                       "value": "{{string}}"
                                    }
                                 },
                                 "variations": [
                                    {
                                       "customPayload": {
                                          "value": "{{string}}"
                                       },
                                       "imageResponseCard": {
                                          "buttons": [
                                             {
                                                "text": "{{string}}",
                                                "value": "{{string}}"
                                             }
                                          ],
                                          "imageUrl": "{{string}}",
                                          "subtitle": "{{string}}",
                                          "title": "{{string}}"
                                       },
                                       "plainTextMessage": {
                                          "value": "{{string}}"
                                       },
                                       "ssmlMessage": {
                                          "value": "{{string}}"
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
                           "slotToElicit": "{{string}}",
                           "suppressNextMessage": {{boolean}},
                           "type": "{{string}}"
                        },
                        "intent": {
                           "name": "{{string}}",
                           "slots": {
                              "{{string}}" : {
                                 "shape": "{{string}}",
                                 "value": {
                                    "interpretedValue": "{{string}}"
                                 },
                                 "values": [
                                    "SlotValueOverride"
                                 ]
                              }
                           }
                        },
                        "sessionAttributes": {
                           "{{string}}" : "{{string}}"
                        }
                     },
                     "response": {
                        "allowInterrupt": {{boolean}},
                        "messageGroups": [
                           {
                              "message": {
                                 "customPayload": {
                                    "value": "{{string}}"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "{{string}}",
                                          "value": "{{string}}"
                                       }
                                    ],
                                    "imageUrl": "{{string}}",
                                    "subtitle": "{{string}}",
                                    "title": "{{string}}"
                                 },
                                 "plainTextMessage": {
                                    "value": "{{string}}"
                                 },
                                 "ssmlMessage": {
                                    "value": "{{string}}"
                                 }
                              },
                              "variations": [
                                 {
                                    "customPayload": {
                                       "value": "{{string}}"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "{{string}}",
                                             "value": "{{string}}"
                                          }
                                       ],
                                       "imageUrl": "{{string}}",
                                       "subtitle": "{{string}}",
                                       "title": "{{string}}"
                                    },
                                    "plainTextMessage": {
                                       "value": "{{string}}"
                                    },
                                    "ssmlMessage": {
                                       "value": "{{string}}"
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
                     "slotToElicit": "{{string}}",
                     "suppressNextMessage": {{boolean}},
                     "type": "{{string}}"
                  },
                  "intent": {
                     "name": "{{string}}",
                     "slots": {
                        "{{string}}" : {
                           "shape": "{{string}}",
                           "value": {
                              "interpretedValue": "{{string}}"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "{{string}}" : "{{string}}"
                  }
               },
               "failureResponse": {
                  "allowInterrupt": {{boolean}},
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "{{string}}"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "{{string}}",
                                    "value": "{{string}}"
                                 }
                              ],
                              "imageUrl": "{{string}}",
                              "subtitle": "{{string}}",
                              "title": "{{string}}"
                           },
                           "plainTextMessage": {
                              "value": "{{string}}"
                           },
                           "ssmlMessage": {
                              "value": "{{string}}"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
                              }
                           }
                        ]
                     }
                  ]
               },
               "successConditional": {
                  "active": {{boolean}},
                  "conditionalBranches": [
                     {
                        "condition": {
                           "expressionString": "{{string}}"
                        },
                        "name": "{{string}}",
                        "nextStep": {
                           "dialogAction": {
                              "slotToElicit": "{{string}}",
                              "suppressNextMessage": {{boolean}},
                              "type": "{{string}}"
                           },
                           "intent": {
                              "name": "{{string}}",
                              "slots": {
                                 "{{string}}" : {
                                    "shape": "{{string}}",
                                    "value": {
                                       "interpretedValue": "{{string}}"
                                    },
                                    "values": [
                                       "SlotValueOverride"
                                    ]
                                 }
                              }
                           },
                           "sessionAttributes": {
                              "{{string}}" : "{{string}}"
                           }
                        },
                        "response": {
                           "allowInterrupt": {{boolean}},
                           "messageGroups": [
                              {
                                 "message": {
                                    "customPayload": {
                                       "value": "{{string}}"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "{{string}}",
                                             "value": "{{string}}"
                                          }
                                       ],
                                       "imageUrl": "{{string}}",
                                       "subtitle": "{{string}}",
                                       "title": "{{string}}"
                                    },
                                    "plainTextMessage": {
                                       "value": "{{string}}"
                                    },
                                    "ssmlMessage": {
                                       "value": "{{string}}"
                                    }
                                 },
                                 "variations": [
                                    {
                                       "customPayload": {
                                          "value": "{{string}}"
                                       },
                                       "imageResponseCard": {
                                          "buttons": [
                                             {
                                                "text": "{{string}}",
                                                "value": "{{string}}"
                                             }
                                          ],
                                          "imageUrl": "{{string}}",
                                          "subtitle": "{{string}}",
                                          "title": "{{string}}"
                                       },
                                       "plainTextMessage": {
                                          "value": "{{string}}"
                                       },
                                       "ssmlMessage": {
                                          "value": "{{string}}"
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
                           "slotToElicit": "{{string}}",
                           "suppressNextMessage": {{boolean}},
                           "type": "{{string}}"
                        },
                        "intent": {
                           "name": "{{string}}",
                           "slots": {
                              "{{string}}" : {
                                 "shape": "{{string}}",
                                 "value": {
                                    "interpretedValue": "{{string}}"
                                 },
                                 "values": [
                                    "SlotValueOverride"
                                 ]
                              }
                           }
                        },
                        "sessionAttributes": {
                           "{{string}}" : "{{string}}"
                        }
                     },
                     "response": {
                        "allowInterrupt": {{boolean}},
                        "messageGroups": [
                           {
                              "message": {
                                 "customPayload": {
                                    "value": "{{string}}"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "{{string}}",
                                          "value": "{{string}}"
                                       }
                                    ],
                                    "imageUrl": "{{string}}",
                                    "subtitle": "{{string}}",
                                    "title": "{{string}}"
                                 },
                                 "plainTextMessage": {
                                    "value": "{{string}}"
                                 },
                                 "ssmlMessage": {
                                    "value": "{{string}}"
                                 }
                              },
                              "variations": [
                                 {
                                    "customPayload": {
                                       "value": "{{string}}"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "{{string}}",
                                             "value": "{{string}}"
                                          }
                                       ],
                                       "imageUrl": "{{string}}",
                                       "subtitle": "{{string}}",
                                       "title": "{{string}}"
                                    },
                                    "plainTextMessage": {
                                       "value": "{{string}}"
                                    },
                                    "ssmlMessage": {
                                       "value": "{{string}}"
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
                     "slotToElicit": "{{string}}",
                     "suppressNextMessage": {{boolean}},
                     "type": "{{string}}"
                  },
                  "intent": {
                     "name": "{{string}}",
                     "slots": {
                        "{{string}}" : {
                           "shape": "{{string}}",
                           "value": {
                              "interpretedValue": "{{string}}"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "{{string}}" : "{{string}}"
                  }
               },
               "successResponse": {
                  "allowInterrupt": {{boolean}},
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "{{string}}"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "{{string}}",
                                    "value": "{{string}}"
                                 }
                              ],
                              "imageUrl": "{{string}}",
                              "subtitle": "{{string}}",
                              "title": "{{string}}"
                           },
                           "plainTextMessage": {
                              "value": "{{string}}"
                           },
                           "ssmlMessage": {
                              "value": "{{string}}"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
                              }
                           }
                        ]
                     }
                  ]
               },
               "timeoutConditional": {
                  "active": {{boolean}},
                  "conditionalBranches": [
                     {
                        "condition": {
                           "expressionString": "{{string}}"
                        },
                        "name": "{{string}}",
                        "nextStep": {
                           "dialogAction": {
                              "slotToElicit": "{{string}}",
                              "suppressNextMessage": {{boolean}},
                              "type": "{{string}}"
                           },
                           "intent": {
                              "name": "{{string}}",
                              "slots": {
                                 "{{string}}" : {
                                    "shape": "{{string}}",
                                    "value": {
                                       "interpretedValue": "{{string}}"
                                    },
                                    "values": [
                                       "SlotValueOverride"
                                    ]
                                 }
                              }
                           },
                           "sessionAttributes": {
                              "{{string}}" : "{{string}}"
                           }
                        },
                        "response": {
                           "allowInterrupt": {{boolean}},
                           "messageGroups": [
                              {
                                 "message": {
                                    "customPayload": {
                                       "value": "{{string}}"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "{{string}}",
                                             "value": "{{string}}"
                                          }
                                       ],
                                       "imageUrl": "{{string}}",
                                       "subtitle": "{{string}}",
                                       "title": "{{string}}"
                                    },
                                    "plainTextMessage": {
                                       "value": "{{string}}"
                                    },
                                    "ssmlMessage": {
                                       "value": "{{string}}"
                                    }
                                 },
                                 "variations": [
                                    {
                                       "customPayload": {
                                          "value": "{{string}}"
                                       },
                                       "imageResponseCard": {
                                          "buttons": [
                                             {
                                                "text": "{{string}}",
                                                "value": "{{string}}"
                                             }
                                          ],
                                          "imageUrl": "{{string}}",
                                          "subtitle": "{{string}}",
                                          "title": "{{string}}"
                                       },
                                       "plainTextMessage": {
                                          "value": "{{string}}"
                                       },
                                       "ssmlMessage": {
                                          "value": "{{string}}"
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
                           "slotToElicit": "{{string}}",
                           "suppressNextMessage": {{boolean}},
                           "type": "{{string}}"
                        },
                        "intent": {
                           "name": "{{string}}",
                           "slots": {
                              "{{string}}" : {
                                 "shape": "{{string}}",
                                 "value": {
                                    "interpretedValue": "{{string}}"
                                 },
                                 "values": [
                                    "SlotValueOverride"
                                 ]
                              }
                           }
                        },
                        "sessionAttributes": {
                           "{{string}}" : "{{string}}"
                        }
                     },
                     "response": {
                        "allowInterrupt": {{boolean}},
                        "messageGroups": [
                           {
                              "message": {
                                 "customPayload": {
                                    "value": "{{string}}"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "{{string}}",
                                          "value": "{{string}}"
                                       }
                                    ],
                                    "imageUrl": "{{string}}",
                                    "subtitle": "{{string}}",
                                    "title": "{{string}}"
                                 },
                                 "plainTextMessage": {
                                    "value": "{{string}}"
                                 },
                                 "ssmlMessage": {
                                    "value": "{{string}}"
                                 }
                              },
                              "variations": [
                                 {
                                    "customPayload": {
                                       "value": "{{string}}"
                                    },
                                    "imageResponseCard": {
                                       "buttons": [
                                          {
                                             "text": "{{string}}",
                                             "value": "{{string}}"
                                          }
                                       ],
                                       "imageUrl": "{{string}}",
                                       "subtitle": "{{string}}",
                                       "title": "{{string}}"
                                    },
                                    "plainTextMessage": {
                                       "value": "{{string}}"
                                    },
                                    "ssmlMessage": {
                                       "value": "{{string}}"
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
                     "slotToElicit": "{{string}}",
                     "suppressNextMessage": {{boolean}},
                     "type": "{{string}}"
                  },
                  "intent": {
                     "name": "{{string}}",
                     "slots": {
                        "{{string}}" : {
                           "shape": "{{string}}",
                           "value": {
                              "interpretedValue": "{{string}}"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "{{string}}" : "{{string}}"
                  }
               },
               "timeoutResponse": {
                  "allowInterrupt": {{boolean}},
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "{{string}}"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "{{string}}",
                                    "value": "{{string}}"
                                 }
                              ],
                              "imageUrl": "{{string}}",
                              "subtitle": "{{string}}",
                              "title": "{{string}}"
                           },
                           "plainTextMessage": {
                              "value": "{{string}}"
                           },
                           "ssmlMessage": {
                              "value": "{{string}}"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
                              }
                           }
                        ]
                     }
                  ]
               }
            }
         },
         "elicitationCodeHook": {
            "enableCodeHookInvocation": {{boolean}},
            "invocationLabel": "{{string}}"
         },
         "failureConditional": {
            "active": {{boolean}},
            "conditionalBranches": [
               {
                  "condition": {
                     "expressionString": "{{string}}"
                  },
                  "name": "{{string}}",
                  "nextStep": {
                     "dialogAction": {
                        "slotToElicit": "{{string}}",
                        "suppressNextMessage": {{boolean}},
                        "type": "{{string}}"
                     },
                     "intent": {
                        "name": "{{string}}",
                        "slots": {
                           "{{string}}" : {
                              "shape": "{{string}}",
                              "value": {
                                 "interpretedValue": "{{string}}"
                              },
                              "values": [
                                 "SlotValueOverride"
                              ]
                           }
                        }
                     },
                     "sessionAttributes": {
                        "{{string}}" : "{{string}}"
                     }
                  },
                  "response": {
                     "allowInterrupt": {{boolean}},
                     "messageGroups": [
                        {
                           "message": {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
                              }
                           },
                           "variations": [
                              {
                                 "customPayload": {
                                    "value": "{{string}}"
                                 },
                                 "imageResponseCard": {
                                    "buttons": [
                                       {
                                          "text": "{{string}}",
                                          "value": "{{string}}"
                                       }
                                    ],
                                    "imageUrl": "{{string}}",
                                    "subtitle": "{{string}}",
                                    "title": "{{string}}"
                                 },
                                 "plainTextMessage": {
                                    "value": "{{string}}"
                                 },
                                 "ssmlMessage": {
                                    "value": "{{string}}"
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
                     "slotToElicit": "{{string}}",
                     "suppressNextMessage": {{boolean}},
                     "type": "{{string}}"
                  },
                  "intent": {
                     "name": "{{string}}",
                     "slots": {
                        "{{string}}" : {
                           "shape": "{{string}}",
                           "value": {
                              "interpretedValue": "{{string}}"
                           },
                           "values": [
                              "SlotValueOverride"
                           ]
                        }
                     }
                  },
                  "sessionAttributes": {
                     "{{string}}" : "{{string}}"
                  }
               },
               "response": {
                  "allowInterrupt": {{boolean}},
                  "messageGroups": [
                     {
                        "message": {
                           "customPayload": {
                              "value": "{{string}}"
                           },
                           "imageResponseCard": {
                              "buttons": [
                                 {
                                    "text": "{{string}}",
                                    "value": "{{string}}"
                                 }
                              ],
                              "imageUrl": "{{string}}",
                              "subtitle": "{{string}}",
                              "title": "{{string}}"
                           },
                           "plainTextMessage": {
                              "value": "{{string}}"
                           },
                           "ssmlMessage": {
                              "value": "{{string}}"
                           }
                        },
                        "variations": [
                           {
                              "customPayload": {
                                 "value": "{{string}}"
                              },
                              "imageResponseCard": {
                                 "buttons": [
                                    {
                                       "text": "{{string}}",
                                       "value": "{{string}}"
                                    }
                                 ],
                                 "imageUrl": "{{string}}",
                                 "subtitle": "{{string}}",
                                 "title": "{{string}}"
                              },
                              "plainTextMessage": {
                                 "value": "{{string}}"
                              },
                              "ssmlMessage": {
                                 "value": "{{string}}"
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
               "slotToElicit": "{{string}}",
               "suppressNextMessage": {{boolean}},
               "type": "{{string}}"
            },
            "intent": {
               "name": "{{string}}",
               "slots": {
                  "{{string}}" : {
                     "shape": "{{string}}",
                     "value": {
                        "interpretedValue": "{{string}}"
                     },
                     "values": [
                        "SlotValueOverride"
                     ]
                  }
               }
            },
            "sessionAttributes": {
               "{{string}}" : "{{string}}"
            }
         },
         "failureResponse": {
            "allowInterrupt": {{boolean}},
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "{{string}}"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "{{string}}",
                              "value": "{{string}}"
                           }
                        ],
                        "imageUrl": "{{string}}",
                        "subtitle": "{{string}}",
                        "title": "{{string}}"
                     },
                     "plainTextMessage": {
                        "value": "{{string}}"
                     },
                     "ssmlMessage": {
                        "value": "{{string}}"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "{{string}}"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "{{string}}",
                                 "value": "{{string}}"
                              }
                           ],
                           "imageUrl": "{{string}}",
                           "subtitle": "{{string}}",
                           "title": "{{string}}"
                        },
                        "plainTextMessage": {
                           "value": "{{string}}"
                        },
                        "ssmlMessage": {
                           "value": "{{string}}"
                        }
                     }
                  ]
               }
            ]
         }
      },
      "slotConstraint": "{{string}}",
      "slotResolutionSetting": {
         "slotResolutionStrategy": "{{string}}"
      },
      "waitAndContinueSpecification": {
         "active": {{boolean}},
         "continueResponse": {
            "allowInterrupt": {{boolean}},
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "{{string}}"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "{{string}}",
                              "value": "{{string}}"
                           }
                        ],
                        "imageUrl": "{{string}}",
                        "subtitle": "{{string}}",
                        "title": "{{string}}"
                     },
                     "plainTextMessage": {
                        "value": "{{string}}"
                     },
                     "ssmlMessage": {
                        "value": "{{string}}"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "{{string}}"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "{{string}}",
                                 "value": "{{string}}"
                              }
                           ],
                           "imageUrl": "{{string}}",
                           "subtitle": "{{string}}",
                           "title": "{{string}}"
                        },
                        "plainTextMessage": {
                           "value": "{{string}}"
                        },
                        "ssmlMessage": {
                           "value": "{{string}}"
                        }
                     }
                  ]
               }
            ]
         },
         "stillWaitingResponse": {
            "allowInterrupt": {{boolean}},
            "frequencyInSeconds": {{number}},
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "{{string}}"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "{{string}}",
                              "value": "{{string}}"
                           }
                        ],
                        "imageUrl": "{{string}}",
                        "subtitle": "{{string}}",
                        "title": "{{string}}"
                     },
                     "plainTextMessage": {
                        "value": "{{string}}"
                     },
                     "ssmlMessage": {
                        "value": "{{string}}"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "{{string}}"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "{{string}}",
                                 "value": "{{string}}"
                              }
                           ],
                           "imageUrl": "{{string}}",
                           "subtitle": "{{string}}",
                           "title": "{{string}}"
                        },
                        "plainTextMessage": {
                           "value": "{{string}}"
                        },
                        "ssmlMessage": {
                           "value": "{{string}}"
                        }
                     }
                  ]
               }
            ],
            "timeoutInSeconds": {{number}}
         },
         "waitingResponse": {
            "allowInterrupt": {{boolean}},
            "messageGroups": [
               {
                  "message": {
                     "customPayload": {
                        "value": "{{string}}"
                     },
                     "imageResponseCard": {
                        "buttons": [
                           {
                              "text": "{{string}}",
                              "value": "{{string}}"
                           }
                        ],
                        "imageUrl": "{{string}}",
                        "subtitle": "{{string}}",
                        "title": "{{string}}"
                     },
                     "plainTextMessage": {
                        "value": "{{string}}"
                     },
                     "ssmlMessage": {
                        "value": "{{string}}"
                     }
                  },
                  "variations": [
                     {
                        "customPayload": {
                           "value": "{{string}}"
                        },
                        "imageResponseCard": {
                           "buttons": [
                              {
                                 "text": "{{string}}",
                                 "value": "{{string}}"
                              }
                           ],
                           "imageUrl": "{{string}}",
                           "subtitle": "{{string}}",
                           "title": "{{string}}"
                        },
                        "plainTextMessage": {
                           "value": "{{string}}"
                        },
                        "ssmlMessage": {
                           "value": "{{string}}"
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

## URI Request Parameters
<a name="API_CreateSlot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-uri-botId"></a>
The identifier of the bot associated with the slot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-uri-botVersion"></a>
The version of the bot associated with the slot.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [intentId](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-uri-intentId"></a>
The identifier of the intent that contains the slot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [localeId](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-uri-localeId"></a>
The identifier of the language and locale that the slot will be used in. The string must match one of the supported locales. All of the bots, intents, slot types used by the slot must have the same locale. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_CreateSlot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-description"></a>
A description of the slot. Use this to help identify the slot in lists.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [multipleValuesSetting](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-multipleValuesSetting"></a>
Indicates whether the slot returns multiple values in one response. Multi-value slots are only available in the `en-US` locale. If you set this value to `true` in any other locale, Amazon Lex throws a `ValidationException`.
If the `multipleValuesSetting` is not set, the default value is `false`.
Type: [MultipleValuesSetting](API_MultipleValuesSetting.md) object
Required: No

 ** [obfuscationSetting](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-obfuscationSetting"></a>
Determines how slot values are used in Amazon CloudWatch logs. If the value of the `obfuscationSetting` parameter is `DefaultObfuscation`, slot values are obfuscated in the log output. If the value is `None`, the actual value is present in the log output.
The default is to obfuscate values in the CloudWatch logs.
Type: [ObfuscationSetting](API_ObfuscationSetting.md) object
Required: No

 ** [slotName](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-slotName"></a>
The name of the slot. Slot names must be unique within the bot that contains the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** [slotTypeId](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-slotTypeId"></a>
The unique identifier for the slot type associated with this slot. The slot type determines the values that can be entered into the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`
Required: No

 ** [subSlotSetting](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-subSlotSetting"></a>
Specifications for the constituent sub slots and the expression for the composite slot.
Type: [SubSlotSetting](API_SubSlotSetting.md) object
Required: No

 ** [valueElicitationSetting](#API_CreateSlot_RequestSyntax) **   <a name="lexv2-CreateSlot-request-valueElicitationSetting"></a>
Specifies prompts that Amazon Lex sends to the user to elicit a response that provides the value for the slot.
Type: [SlotValueElicitationSetting](API_SlotValueElicitationSetting.md) object
Required: Yes

## Response Syntax
<a name="API_CreateSlot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "description": "string",
   "intentId": "string",
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
<a name="API_CreateSlot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-botId"></a>
The unique identifier of the bot associated with the slot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-botVersion"></a>
The version of the bot associated with the slot.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [creationDateTime](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-creationDateTime"></a>
The timestamp of the date and time that the slot was created.
Type: Timestamp

 ** [description](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-description"></a>
The description associated with the slot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [intentId](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-intentId"></a>
The unique identifier of the intent associated with the slot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [localeId](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-localeId"></a>
The language and local specified for the slot.
Type: String

 ** [multipleValuesSetting](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-multipleValuesSetting"></a>
Indicates whether the slot returns multiple values in one response.
Type: [MultipleValuesSetting](API_MultipleValuesSetting.md) object

 ** [obfuscationSetting](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-obfuscationSetting"></a>
Indicates whether the slot is configured to obfuscate values in Amazon CloudWatch logs.
Type: [ObfuscationSetting](API_ObfuscationSetting.md) object

 ** [slotId](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-slotId"></a>
The unique identifier associated with the slot. Use this to identify the slot when you update or delete it.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [slotName](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-slotName"></a>
The name specified for the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [slotTypeId](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-slotTypeId"></a>
The unique identifier of the slot type associated with this slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`

 ** [subSlotSetting](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-subSlotSetting"></a>
Specifications for the constituent sub slots and the expression for the composite slot.
Type: [SubSlotSetting](API_SubSlotSetting.md) object

 ** [valueElicitationSetting](#API_CreateSlot_ResponseSyntax) **   <a name="lexv2-CreateSlot-response-valueElicitationSetting"></a>
The value elicitation settings specified for the slot.
Type: [SlotValueElicitationSetting](API_SlotValueElicitationSetting.md) object

## Errors
<a name="API_CreateSlot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

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
<a name="API_CreateSlot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/CreateSlot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/CreateSlot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CreateSlot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/CreateSlot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CreateSlot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/CreateSlot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/CreateSlot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/CreateSlot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/CreateSlot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CreateSlot)
