---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html
---

# CreateIntent
<a name="API_CreateIntent"></a>

Creates an intent.

To define the interaction between the user and your bot, you define one or more intents. For example, for a pizza ordering bot you would create an `OrderPizza` intent.

When you create an intent, you must provide a name. You can optionally provide the following:
+ Sample utterances. For example, "I want to order a pizza" and "Can I order a pizza." You can't provide utterances for built-in intents.
+ Information to be gathered. You specify slots for the information that you bot requests from the user. You can specify standard slot types, such as date and time, or custom slot types for your application.
+ How the intent is fulfilled. You can provide a Lambda function or configure the intent to return the intent information to your client application. If you use a Lambda function, Amazon Lex invokes the function when all of the intent information is available.
+ A confirmation prompt to send to the user to confirm an intent. For example, "Shall I order your pizza?"
+ A conclusion statement to send to the user after the intent is fulfilled. For example, "I ordered your pizza."
+ A follow-up prompt that asks the user for additional activity. For example, "Do you want a drink with your pizza?"

## Request Syntax
<a name="API_CreateIntent_RequestSyntax"></a>

```
PUT /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/intents/ HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "dialogCodeHook": {
      "enabled": {{boolean}}
   },
   "fulfillmentCodeHook": {
      "active": {{boolean}},
      "enabled": {{boolean}},
      "fulfillmentUpdatesSpecification": {
         "active": {{boolean}},
         "startResponse": {
            "allowInterrupt": {{boolean}},
            "delayInSeconds": {{number}},
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
         "timeoutInSeconds": {{number}},
         "updateResponse": {
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
            ]
         }
      },
      "postFulfillmentStatusSpecification": {
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
   "initialResponseSetting": {
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
      "conditional": {
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
      "initialResponse": {
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
      }
   },
   "inputContexts": [
      {
         "name": "{{string}}"
      }
   ],
   "intentClosingSetting": {
      "active": {{boolean}},
      "closingResponse": {
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
      "conditional": {
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
      }
   },
   "intentConfirmationSetting": {
      "active": {{boolean}},
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
      "confirmationConditional": {
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
      "confirmationNextStep": {
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
      "confirmationResponse": {
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
      "declinationConditional": {
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
      "declinationNextStep": {
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
      "declinationResponse": {
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
      }
   },
   "intentDisplayName": "{{string}}",
   "intentName": "{{string}}",
   "kendraConfiguration": {
      "kendraIndex": "{{string}}",
      "queryFilterString": "{{string}}",
      "queryFilterStringEnabled": {{boolean}}
   },
   "outputContexts": [
      {
         "name": "{{string}}",
         "timeToLiveInSeconds": {{number}},
         "turnsToLive": {{number}}
      }
   ],
   "parentIntentSignature": "{{string}}",
   "qInConnectIntentConfiguration": {
      "qInConnectAssistantConfiguration": {
         "assistantArn": "{{string}}"
      }
   },
   "qnAIntentConfiguration": {
      "bedrockModelConfiguration": {
         "customPrompt": "{{string}}",
         "guardrail": {
            "identifier": "{{string}}",
            "version": "{{string}}"
         },
         "modelArn": "{{string}}",
         "traceStatus": "{{string}}"
      },
      "dataSourceConfiguration": {
         "bedrockKnowledgeStoreConfiguration": {
            "bedrockKnowledgeBaseArn": "{{string}}",
            "exactResponse": {{boolean}},
            "exactResponseFields": {
               "answerField": "{{string}}"
            }
         },
         "kendraConfiguration": {
            "exactResponse": {{boolean}},
            "kendraIndex": "{{string}}",
            "queryFilterString": "{{string}}",
            "queryFilterStringEnabled": {{boolean}}
         },
         "opensearchConfiguration": {
            "domainEndpoint": "{{string}}",
            "exactResponse": {{boolean}},
            "exactResponseFields": {
               "answerField": "{{string}}",
               "questionField": "{{string}}"
            },
            "includeFields": [ "{{string}}" ],
            "indexName": "{{string}}"
         }
      }
   },
   "sampleUtterances": [
      {
         "utterance": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateIntent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-uri-botId"></a>
The identifier of the bot associated with this intent.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-uri-botVersion"></a>
The version of the bot associated with this intent.
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`
Required: Yes

 ** [localeId](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-uri-localeId"></a>
The identifier of the language and locale where this intent is used. All of the bots, slot types, and slots used by the intent must have the same locale. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_CreateIntent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-description"></a>
A description of the intent. Use the description to help identify the intent in lists.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [dialogCodeHook](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-dialogCodeHook"></a>
Specifies that Amazon Lex invokes the alias Lambda function for each user input. You can invoke this Lambda function to personalize user interaction.
For example, suppose that your bot determines that the user's name is John. You Lambda function might retrieve John's information from a backend database and prepopulate some of the values. For example, if you find that John is gluten intolerant, you might set the corresponding intent slot, `glutenIntolerant` to `true`. You might find John's phone number and set the corresponding session attribute.
Type: [DialogCodeHookSettings](API_DialogCodeHookSettings.md) object
Required: No

 ** [fulfillmentCodeHook](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-fulfillmentCodeHook"></a>
Specifies that Amazon Lex invokes the alias Lambda function when the intent is ready for fulfillment. You can invoke this function to complete the bot's transaction with the user.
For example, in a pizza ordering bot, the Lambda function can look up the closest pizza restaurant to the customer's location and then place an order on the customer's behalf.
Type: [FulfillmentCodeHookSettings](API_FulfillmentCodeHookSettings.md) object
Required: No

 ** [initialResponseSetting](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-initialResponseSetting"></a>
Configuration settings for the response that is sent to the user at the beginning of a conversation, before eliciting slot values.
Type: [InitialResponseSetting](API_InitialResponseSetting.md) object
Required: No

 ** [inputContexts](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-inputContexts"></a>
A list of contexts that must be active for this intent to be considered by Amazon Lex.
When an intent has an input context list, Amazon Lex only considers using the intent in an interaction with the user when the specified contexts are included in the active context list for the session. If the contexts are not active, then Amazon Lex will not use the intent.
A context can be automatically activated using the `outputContexts` property or it can be set at runtime.
 For example, if there are two intents with different input contexts that respond to the same utterances, only the intent with the active context will respond.
An intent may have up to 5 input contexts. If an intent has multiple input contexts, all of the contexts must be active to consider the intent.
Type: Array of [InputContext](API_InputContext.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [intentClosingSetting](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-intentClosingSetting"></a>
Sets the response that Amazon Lex sends to the user when the intent is closed.
Type: [IntentClosingSetting](API_IntentClosingSetting.md) object
Required: No

 ** [intentConfirmationSetting](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-intentConfirmationSetting"></a>
Provides prompts that Amazon Lex sends to the user to confirm the completion of an intent. If the user answers "no," the settings contain a statement that is sent to the user to end the intent.
Type: [IntentConfirmationSetting](API_IntentConfirmationSetting.md) object
Required: No

 ** [intentDisplayName](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-intentDisplayName"></a>
A display name for the intent. If configured, This name will be shown to users during Intent Disambiguation instead of the intent name. Display names should be user-friendly, descriptive and match the intent's purpose to improve user experience during disambiguation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [intentName](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-intentName"></a>
The name of the intent. Intent names must be unique in the locale that contains the intent and cannot match the name of any built-in intent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** [kendraConfiguration](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-kendraConfiguration"></a>
Configuration information required to use the `AMAZON.KendraSearchIntent` intent to connect to an Amazon Kendra index. The `AMAZON.KendraSearchIntent` intent is called when Amazon Lex can't determine another intent to invoke.
Type: [KendraConfiguration](API_KendraConfiguration.md) object
Required: No

 ** [outputContexts](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-outputContexts"></a>
A lists of contexts that the intent activates when it is fulfilled.
You can use an output context to indicate the intents that Amazon Lex should consider for the next turn of the conversation with a customer.
When you use the `outputContextsList` property, all of the contexts specified in the list are activated when the intent is fulfilled. You can set up to 10 output contexts. You can also set the number of conversation turns that the context should be active, or the length of time that the context should be active.
Type: Array of [OutputContext](API_OutputContext.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [parentIntentSignature](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-parentIntentSignature"></a>
A unique identifier for the built-in intent to base this intent on.
Type: String
Required: No

 ** [qInConnectIntentConfiguration](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-qInConnectIntentConfiguration"></a>
Qinconnect intent configuration details for the create intent request.
Type: [QInConnectIntentConfiguration](API_QInConnectIntentConfiguration.md) object
Required: No

 ** [qnAIntentConfiguration](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-qnAIntentConfiguration"></a>
Specifies the configuration of the built-in `Amazon.QnAIntent`. The `AMAZON.QnAIntent` intent is called when Amazon Lex can't determine another intent to invoke. If you specify this field, you can't specify the `kendraConfiguration` field.
Type: [QnAIntentConfiguration](API_QnAIntentConfiguration.md) object
Required: No

 ** [sampleUtterances](#API_CreateIntent_RequestSyntax) **   <a name="lexv2-CreateIntent-request-sampleUtterances"></a>
An array of strings that a user might say to signal the intent. For example, "I want a pizza", or "I want a {PizzaSize} pizza".
In an utterance, slot names are enclosed in curly braces ("{", "}") to indicate where they should be displayed in the utterance shown to the user..
Type: Array of [SampleUtterance](API_SampleUtterance.md) objects
Required: No

## Response Syntax
<a name="API_CreateIntent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "botVersion": "string",
   "creationDateTime": number,
   "description": "string",
   "dialogCodeHook": {
      "enabled": boolean
   },
   "fulfillmentCodeHook": {
      "active": boolean,
      "enabled": boolean,
      "fulfillmentUpdatesSpecification": {
         "active": boolean,
         "startResponse": {
            "allowInterrupt": boolean,
            "delayInSeconds": number,
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
         "timeoutInSeconds": number,
         "updateResponse": {
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
            ]
         }
      },
      "postFulfillmentStatusSpecification": {
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
   "initialResponseSetting": {
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
      "conditional": {
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
      "initialResponse": {
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
      }
   },
   "inputContexts": [
      {
         "name": "string"
      }
   ],
   "intentClosingSetting": {
      "active": boolean,
      "closingResponse": {
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
      "conditional": {
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
      }
   },
   "intentConfirmationSetting": {
      "active": boolean,
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
      "confirmationConditional": {
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
      "confirmationNextStep": {
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
      "confirmationResponse": {
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
      "declinationConditional": {
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
      "declinationNextStep": {
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
      "declinationResponse": {
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
      }
   },
   "intentDisplayName": "string",
   "intentId": "string",
   "intentName": "string",
   "kendraConfiguration": {
      "kendraIndex": "string",
      "queryFilterString": "string",
      "queryFilterStringEnabled": boolean
   },
   "localeId": "string",
   "outputContexts": [
      {
         "name": "string",
         "timeToLiveInSeconds": number,
         "turnsToLive": number
      }
   ],
   "parentIntentSignature": "string",
   "qInConnectIntentConfiguration": {
      "qInConnectAssistantConfiguration": {
         "assistantArn": "string"
      }
   },
   "qnAIntentConfiguration": {
      "bedrockModelConfiguration": {
         "customPrompt": "string",
         "guardrail": {
            "identifier": "string",
            "version": "string"
         },
         "modelArn": "string",
         "traceStatus": "string"
      },
      "dataSourceConfiguration": {
         "bedrockKnowledgeStoreConfiguration": {
            "bedrockKnowledgeBaseArn": "string",
            "exactResponse": boolean,
            "exactResponseFields": {
               "answerField": "string"
            }
         },
         "kendraConfiguration": {
            "exactResponse": boolean,
            "kendraIndex": "string",
            "queryFilterString": "string",
            "queryFilterStringEnabled": boolean
         },
         "opensearchConfiguration": {
            "domainEndpoint": "string",
            "exactResponse": boolean,
            "exactResponseFields": {
               "answerField": "string",
               "questionField": "string"
            },
            "includeFields": [ "string" ],
            "indexName": "string"
         }
      }
   },
   "sampleUtterances": [
      {
         "utterance": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateIntent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-botId"></a>
The identifier of the bot associated with the intent.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-botVersion"></a>
The version of the bot associated with the intent.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [creationDateTime](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-creationDateTime"></a>
A timestamp of the date and time that the intent was created.
Type: Timestamp

 ** [description](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-description"></a>
The description specified for the intent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [dialogCodeHook](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-dialogCodeHook"></a>
The dialog Lambda function specified for the intent.
Type: [DialogCodeHookSettings](API_DialogCodeHookSettings.md) object

 ** [fulfillmentCodeHook](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-fulfillmentCodeHook"></a>
The fulfillment Lambda function specified for the intent.
Type: [FulfillmentCodeHookSettings](API_FulfillmentCodeHookSettings.md) object

 ** [initialResponseSetting](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-initialResponseSetting"></a>
Configuration settings for the response that is sent to the user at the beginning of a conversation, before eliciting slot values.
Type: [InitialResponseSetting](API_InitialResponseSetting.md) object

 ** [inputContexts](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-inputContexts"></a>
The list of input contexts specified for the intent.
Type: Array of [InputContext](API_InputContext.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [intentClosingSetting](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-intentClosingSetting"></a>
The closing setting specified for the intent.
Type: [IntentClosingSetting](API_IntentClosingSetting.md) object

 ** [intentConfirmationSetting](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-intentConfirmationSetting"></a>
The confirmation setting specified for the intent.
Type: [IntentConfirmationSetting](API_IntentConfirmationSetting.md) object

 ** [intentDisplayName](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-intentDisplayName"></a>
The display name specified for the intent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [intentId](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-intentId"></a>
A unique identifier for the intent.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [intentName](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-intentName"></a>
The name specified for the intent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [kendraConfiguration](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-kendraConfiguration"></a>
Configuration for searching a Amazon Kendra index specified for the intent.
Type: [KendraConfiguration](API_KendraConfiguration.md) object

 ** [localeId](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-localeId"></a>
The locale that the intent is specified to use.
Type: String

 ** [outputContexts](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-outputContexts"></a>
The list of output contexts specified for the intent.
Type: Array of [OutputContext](API_OutputContext.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [parentIntentSignature](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-parentIntentSignature"></a>
The signature of the parent intent specified for the intent.
Type: String

 ** [qInConnectIntentConfiguration](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-qInConnectIntentConfiguration"></a>
Qinconnect intent configuration details for the create intent response.
Type: [QInConnectIntentConfiguration](API_QInConnectIntentConfiguration.md) object

 ** [qnAIntentConfiguration](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-qnAIntentConfiguration"></a>
Details about the the configuration of the built-in `Amazon.QnAIntent`.
Type: [QnAIntentConfiguration](API_QnAIntentConfiguration.md) object

 ** [sampleUtterances](#API_CreateIntent_ResponseSyntax) **   <a name="lexv2-CreateIntent-response-sampleUtterances"></a>
The sample utterances specified for the intent.
Type: Array of [SampleUtterance](API_SampleUtterance.md) objects

## Errors
<a name="API_CreateIntent_Errors"></a>

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
<a name="API_CreateIntent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/CreateIntent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/CreateIntent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CreateIntent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/CreateIntent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CreateIntent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/CreateIntent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/CreateIntent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/CreateIntent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/CreateIntent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CreateIntent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
