---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeIntent.html
---

# DescribeIntent
<a name="API_DescribeIntent"></a>

Returns metadata about an intent.

## Request Syntax
<a name="API_DescribeIntent_RequestSyntax"></a>

```
GET /bots/{{botId}}/botversions/{{botVersion}}/botlocales/{{localeId}}/intents/{{intentId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeIntent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_DescribeIntent_RequestSyntax) **   <a name="lexv2-DescribeIntent-request-uri-botId"></a>
The identifier of the bot associated with the intent.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [botVersion](#API_DescribeIntent_RequestSyntax) **   <a name="lexv2-DescribeIntent-request-uri-botVersion"></a>
The version of the bot associated with the intent.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** [intentId](#API_DescribeIntent_RequestSyntax) **   <a name="lexv2-DescribeIntent-request-uri-intentId"></a>
The identifier of the intent to describe.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** [localeId](#API_DescribeIntent_RequestSyntax) **   <a name="lexv2-DescribeIntent-request-uri-localeId"></a>
The identifier of the language and locale of the intent to describe. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
Required: Yes

## Request Body
<a name="API_DescribeIntent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeIntent_ResponseSyntax"></a>

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
   "lastUpdatedDateTime": number,
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
   ],
   "slotPriorities": [
      {
         "priority": number,
         "slotId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeIntent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-botId"></a>
The identifier of the bot associated with the intent.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [botVersion](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-botVersion"></a>
The version of the bot associated with the intent.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `^DRAFT$`

 ** [creationDateTime](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-creationDateTime"></a>
A timestamp of the date and time that the intent was created.
Type: Timestamp

 ** [description](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-description"></a>
The description of the intent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [dialogCodeHook](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-dialogCodeHook"></a>
The Lambda function called during each turn of a conversation with the intent.
Type: [DialogCodeHookSettings](API_DialogCodeHookSettings.md) object

 ** [fulfillmentCodeHook](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-fulfillmentCodeHook"></a>
The Lambda function called when the intent is complete and ready for fulfillment.
Type: [FulfillmentCodeHookSettings](API_FulfillmentCodeHookSettings.md) object

 ** [initialResponseSetting](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-initialResponseSetting"></a>
Configuration setting for a response sent to the user before Amazon Lex starts eliciting slots.
Type: [InitialResponseSetting](API_InitialResponseSetting.md) object

 ** [inputContexts](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-inputContexts"></a>
A list of contexts that must be active for the intent to be considered for sending to the user.
Type: Array of [InputContext](API_InputContext.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [intentClosingSetting](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-intentClosingSetting"></a>
The response that Amazon Lex sends to when the intent is closed.
Type: [IntentClosingSetting](API_IntentClosingSetting.md) object

 ** [intentConfirmationSetting](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-intentConfirmationSetting"></a>
Prompts that Amazon Lex sends to the user to confirm completion of an intent.
Type: [IntentConfirmationSetting](API_IntentConfirmationSetting.md) object

 ** [intentDisplayName](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-intentDisplayName"></a>
The display name specified for the intent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [intentId](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-intentId"></a>
The unique identifier assigned to the intent when it was created.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [intentName](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-intentName"></a>
The name specified for the intent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [kendraConfiguration](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-kendraConfiguration"></a>
Configuration information required to use the `AMAZON.KendraSearchIntent` intent.
Type: [KendraConfiguration](API_KendraConfiguration.md) object

 ** [lastUpdatedDateTime](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-lastUpdatedDateTime"></a>
A timestamp of the date and time that the intent was last updated.
Type: Timestamp

 ** [localeId](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-localeId"></a>
The language and locale specified for the intent.
Type: String

 ** [outputContexts](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-outputContexts"></a>
A list of contexts that are activated when the intent is fulfilled.
Type: Array of [OutputContext](API_OutputContext.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [parentIntentSignature](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-parentIntentSignature"></a>
The identifier of the built-in intent that this intent is derived from, if any.
Type: String

 ** [qInConnectIntentConfiguration](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-qInConnectIntentConfiguration"></a>
Qinconnect intent configuration details for the describe intent response.
Type: [QInConnectIntentConfiguration](API_QInConnectIntentConfiguration.md) object

 ** [qnAIntentConfiguration](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-qnAIntentConfiguration"></a>
Details about the configuration of the built-in `Amazon.QnAIntent`.
Type: [QnAIntentConfiguration](API_QnAIntentConfiguration.md) object

 ** [sampleUtterances](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-sampleUtterances"></a>
User utterances that trigger this intent.
Type: Array of [SampleUtterance](API_SampleUtterance.md) objects

 ** [slotPriorities](#API_DescribeIntent_ResponseSyntax) **   <a name="lexv2-DescribeIntent-response-slotPriorities"></a>
The list that determines the priority that slots should be elicited from the user.
Type: Array of [SlotPriority](API_SlotPriority.md) objects

## Errors
<a name="API_DescribeIntent_Errors"></a>

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
<a name="API_DescribeIntent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeIntent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeIntent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeIntent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeIntent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeIntent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeIntent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeIntent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeIntent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeIntent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeIntent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
