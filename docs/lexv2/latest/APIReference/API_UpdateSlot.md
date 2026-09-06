---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateSlot.html
---

# UpdateSlot
<a name="API_UpdateSlot"></a>

Updates the settings for a slot.

## Request Syntax
<a name="API_UpdateSlot_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/intents/{{intentId}}/slots/{{slotId}}/ HTTP/1.1
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
<a name="API_UpdateSlot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-uri-botId"></a>
The unique identifier of the bot that contains the slot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-uri-botVersion"></a>
The version of the bot that contains the slot. Must always be `DRAFT`.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [intentId](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-uri-intentId"></a>
The identifier of the intent that contains the slot.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [localeId](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-uri-localeId"></a>
The identifier of the language and locale that contains the slot. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

 ** [slotId](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-uri-slotId"></a>
The unique identifier for the slot to update.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_UpdateSlot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-description"></a>
The new description for the slot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [multipleValuesSetting](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-multipleValuesSetting"></a>
Determines whether the slot accepts multiple values in one response. Multiple value slots are only available in the en-US locale. If you set this value to `true` in any other locale, Amazon Lex throws a `ValidationException`.
If the `multipleValuesSetting` is not set, the default value is `false`.
Type: [MultipleValuesSetting](API_MultipleValuesSetting.md) object
Required: No

 ** [obfuscationSetting](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-obfuscationSetting"></a>
New settings that determine how slot values are formatted in Amazon CloudWatch logs.
Type: [ObfuscationSetting](API_ObfuscationSetting.md) object
Required: No

 ** [slotName](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-slotName"></a>
The new name for the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** [slotTypeId](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-slotTypeId"></a>
The unique identifier of the new slot type to associate with this slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`
Required: No

 ** [subSlotSetting](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-subSlotSetting"></a>
Specifications for the constituent sub slots and the expression for the composite slot.
Type: [SubSlotSetting](API_SubSlotSetting.md) object
Required: No

 ** [valueElicitationSetting](#API_UpdateSlot_RequestSyntax) **   <a name="lexv2-UpdateSlot-request-valueElicitationSetting"></a>
A new set of prompts that Amazon Lex sends to the user to elicit a response the provides a value for the slot.
Type: [SlotValueElicitationSetting](API_SlotValueElicitationSetting.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateSlot_ResponseSyntax"></a>

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
<a name="API_UpdateSlot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-botId"></a>
The identifier of the bot that contains the slot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-botVersion"></a>
The version of the bot that contains the slot. Will always be `DRAFT`.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [creationDateTime](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-creationDateTime"></a>
The timestamp of the date and time that the slot was created.
Type: Timestamp

 ** [description](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-description"></a>
The updated description of the bot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [intentId](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-intentId"></a>
The intent that contains the slot.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [lastUpdatedDateTime](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-lastUpdatedDateTime"></a>
The timestamp of the date and time that the slot was last updated.
Type: Timestamp

 ** [localeId](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-localeId"></a>
The locale that contains the slot.
Type: String

 ** [multipleValuesSetting](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-multipleValuesSetting"></a>
Indicates whether the slot accepts multiple values in one response.
Type: [MultipleValuesSetting](API_MultipleValuesSetting.md) object

 ** [obfuscationSetting](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-obfuscationSetting"></a>
The updated setting that determines whether the slot value is obfuscated in the Amazon CloudWatch logs.
Type: [ObfuscationSetting](API_ObfuscationSetting.md) object

 ** [slotId](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-slotId"></a>
The unique identifier of the slot that was updated.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [slotName](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-slotName"></a>
The updated name of the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [slotTypeId](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-slotTypeId"></a>
The updated identifier of the slot type that provides values for the slot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^((AMAZON\.)[a-zA-Z_]+?|[0-9a-zA-Z]+)$`

 ** [subSlotSetting](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-subSlotSetting"></a>
Specifications for the constituent sub slots and the expression for the composite slot.
Type: [SubSlotSetting](API_SubSlotSetting.md) object

 ** [valueElicitationSetting](#API_UpdateSlot_ResponseSyntax) **   <a name="lexv2-UpdateSlot-response-valueElicitationSetting"></a>
The updated prompts that Amazon Lex sends to the user to elicit a response that provides a value for the slot.
Type: [SlotValueElicitationSetting](API_SlotValueElicitationSetting.md) object

## Errors
<a name="API_UpdateSlot_Errors"></a>

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
<a name="API_UpdateSlot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/UpdateSlot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/UpdateSlot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UpdateSlot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/UpdateSlot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UpdateSlot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/UpdateSlot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/UpdateSlot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/UpdateSlot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/UpdateSlot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UpdateSlot)
