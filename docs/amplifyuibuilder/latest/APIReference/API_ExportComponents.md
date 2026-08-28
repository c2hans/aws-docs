---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ExportComponents.html
---

# ExportComponents
<a name="API_ExportComponents"></a>

Exports component configurations to code that is ready to integrate into an Amplify app.

## Request Syntax
<a name="API_ExportComponents_RequestSyntax"></a>

```
GET /export/app/{{appId}}/environment/{{environmentName}}/components?nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ExportComponents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_ExportComponents_RequestSyntax) **   <a name="amplifyuibuilder-ExportComponents-request-uri-appId"></a>
The unique ID of the Amplify app to export components to.
Required: Yes

 ** [environmentName](#API_ExportComponents_RequestSyntax) **   <a name="amplifyuibuilder-ExportComponents-request-uri-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Required: Yes

 ** [nextToken](#API_ExportComponents_RequestSyntax) **   <a name="amplifyuibuilder-ExportComponents-request-uri-nextToken"></a>
The token to request the next page of results.

## Request Body
<a name="API_ExportComponents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ExportComponents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "entities": [
      {
         "appId": "string",
         "bindingProperties": {
            "string" : {
               "bindingProperties": {
                  "bucket": "string",
                  "defaultValue": "string",
                  "field": "string",
                  "key": "string",
                  "model": "string",
                  "predicates": [
                     {
                        "and": [
                           "Predicate"
                        ],
                        "field": "string",
                        "operand": "string",
                        "operandType": "string",
                        "operator": "string",
                        "or": [
                           "Predicate"
                        ]
                     }
                  ],
                  "slotName": "string",
                  "userAttribute": "string"
               },
               "defaultValue": "string",
               "type": "string"
            }
         },
         "children": [
            {
               "children": [
                  "ComponentChild"
               ],
               "componentType": "string",
               "events": {
                  "string" : {
                     "action": "string",
                     "bindingEvent": "string",
                     "parameters": {
                        "anchor": {
                           "bindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "bindings": {
                              "string" : {
                                 "element": "string",
                                 "property": "string"
                              }
                           },
                           "collectionBindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "componentName": "string",
                           "concat": [
                              "ComponentProperty"
                           ],
                           "condition": {
                              "else": "ComponentProperty",
                              "field": "string",
                              "operand": "string",
                              "operandType": "string",
                              "operator": "string",
                              "property": "string",
                              "then": "ComponentProperty"
                           },
                           "configured": boolean,
                           "defaultValue": "string",
                           "event": "string",
                           "importedValue": "string",
                           "model": "string",
                           "property": "string",
                           "type": "string",
                           "userAttribute": "string",
                           "value": "string"
                        },
                        "fields": {
                           "string" : {
                              "bindingProperties": {
                                 "field": "string",
                                 "property": "string"
                              },
                              "bindings": {
                                 "string" : {
                                    "element": "string",
                                    "property": "string"
                                 }
                              },
                              "collectionBindingProperties": {
                                 "field": "string",
                                 "property": "string"
                              },
                              "componentName": "string",
                              "concat": [
                                 "ComponentProperty"
                              ],
                              "condition": {
                                 "else": "ComponentProperty",
                                 "field": "string",
                                 "operand": "string",
                                 "operandType": "string",
                                 "operator": "string",
                                 "property": "string",
                                 "then": "ComponentProperty"
                              },
                              "configured": boolean,
                              "defaultValue": "string",
                              "event": "string",
                              "importedValue": "string",
                              "model": "string",
                              "property": "string",
                              "type": "string",
                              "userAttribute": "string",
                              "value": "string"
                           }
                        },
                        "global": {
                           "bindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "bindings": {
                              "string" : {
                                 "element": "string",
                                 "property": "string"
                              }
                           },
                           "collectionBindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "componentName": "string",
                           "concat": [
                              "ComponentProperty"
                           ],
                           "condition": {
                              "else": "ComponentProperty",
                              "field": "string",
                              "operand": "string",
                              "operandType": "string",
                              "operator": "string",
                              "property": "string",
                              "then": "ComponentProperty"
                           },
                           "configured": boolean,
                           "defaultValue": "string",
                           "event": "string",
                           "importedValue": "string",
                           "model": "string",
                           "property": "string",
                           "type": "string",
                           "userAttribute": "string",
                           "value": "string"
                        },
                        "id": {
                           "bindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "bindings": {
                              "string" : {
                                 "element": "string",
                                 "property": "string"
                              }
                           },
                           "collectionBindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "componentName": "string",
                           "concat": [
                              "ComponentProperty"
                           ],
                           "condition": {
                              "else": "ComponentProperty",
                              "field": "string",
                              "operand": "string",
                              "operandType": "string",
                              "operator": "string",
                              "property": "string",
                              "then": "ComponentProperty"
                           },
                           "configured": boolean,
                           "defaultValue": "string",
                           "event": "string",
                           "importedValue": "string",
                           "model": "string",
                           "property": "string",
                           "type": "string",
                           "userAttribute": "string",
                           "value": "string"
                        },
                        "model": "string",
                        "state": {
                           "componentName": "string",
                           "property": "string",
                           "set": {
                              "bindingProperties": {
                                 "field": "string",
                                 "property": "string"
                              },
                              "bindings": {
                                 "string" : {
                                    "element": "string",
                                    "property": "string"
                                 }
                              },
                              "collectionBindingProperties": {
                                 "field": "string",
                                 "property": "string"
                              },
                              "componentName": "string",
                              "concat": [
                                 "ComponentProperty"
                              ],
                              "condition": {
                                 "else": "ComponentProperty",
                                 "field": "string",
                                 "operand": "string",
                                 "operandType": "string",
                                 "operator": "string",
                                 "property": "string",
                                 "then": "ComponentProperty"
                              },
                              "configured": boolean,
                              "defaultValue": "string",
                              "event": "string",
                              "importedValue": "string",
                              "model": "string",
                              "property": "string",
                              "type": "string",
                              "userAttribute": "string",
                              "value": "string"
                           }
                        },
                        "target": {
                           "bindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "bindings": {
                              "string" : {
                                 "element": "string",
                                 "property": "string"
                              }
                           },
                           "collectionBindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "componentName": "string",
                           "concat": [
                              "ComponentProperty"
                           ],
                           "condition": {
                              "else": "ComponentProperty",
                              "field": "string",
                              "operand": "string",
                              "operandType": "string",
                              "operator": "string",
                              "property": "string",
                              "then": "ComponentProperty"
                           },
                           "configured": boolean,
                           "defaultValue": "string",
                           "event": "string",
                           "importedValue": "string",
                           "model": "string",
                           "property": "string",
                           "type": "string",
                           "userAttribute": "string",
                           "value": "string"
                        },
                        "type": {
                           "bindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "bindings": {
                              "string" : {
                                 "element": "string",
                                 "property": "string"
                              }
                           },
                           "collectionBindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "componentName": "string",
                           "concat": [
                              "ComponentProperty"
                           ],
                           "condition": {
                              "else": "ComponentProperty",
                              "field": "string",
                              "operand": "string",
                              "operandType": "string",
                              "operator": "string",
                              "property": "string",
                              "then": "ComponentProperty"
                           },
                           "configured": boolean,
                           "defaultValue": "string",
                           "event": "string",
                           "importedValue": "string",
                           "model": "string",
                           "property": "string",
                           "type": "string",
                           "userAttribute": "string",
                           "value": "string"
                        },
                        "url": {
                           "bindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "bindings": {
                              "string" : {
                                 "element": "string",
                                 "property": "string"
                              }
                           },
                           "collectionBindingProperties": {
                              "field": "string",
                              "property": "string"
                           },
                           "componentName": "string",
                           "concat": [
                              "ComponentProperty"
                           ],
                           "condition": {
                              "else": "ComponentProperty",
                              "field": "string",
                              "operand": "string",
                              "operandType": "string",
                              "operator": "string",
                              "property": "string",
                              "then": "ComponentProperty"
                           },
                           "configured": boolean,
                           "defaultValue": "string",
                           "event": "string",
                           "importedValue": "string",
                           "model": "string",
                           "property": "string",
                           "type": "string",
                           "userAttribute": "string",
                           "value": "string"
                        }
                     }
                  }
               },
               "name": "string",
               "properties": {
                  "string" : {
                     "bindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "bindings": {
                        "string" : {
                           "element": "string",
                           "property": "string"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "componentName": "string",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "string",
                        "operand": "string",
                        "operandType": "string",
                        "operator": "string",
                        "property": "string",
                        "then": "ComponentProperty"
                     },
                     "configured": boolean,
                     "defaultValue": "string",
                     "event": "string",
                     "importedValue": "string",
                     "model": "string",
                     "property": "string",
                     "type": "string",
                     "userAttribute": "string",
                     "value": "string"
                  }
               },
               "sourceId": "string"
            }
         ],
         "collectionProperties": {
            "string" : {
               "identifiers": [ "string" ],
               "model": "string",
               "predicate": {
                  "and": [
                     "Predicate"
                  ],
                  "field": "string",
                  "operand": "string",
                  "operandType": "string",
                  "operator": "string",
                  "or": [
                     "Predicate"
                  ]
               },
               "sort": [
                  {
                     "direction": "string",
                     "field": "string"
                  }
               ]
            }
         },
         "componentType": "string",
         "createdAt": "string",
         "environmentName": "string",
         "events": {
            "string" : {
               "action": "string",
               "bindingEvent": "string",
               "parameters": {
                  "anchor": {
                     "bindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "bindings": {
                        "string" : {
                           "element": "string",
                           "property": "string"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "componentName": "string",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "string",
                        "operand": "string",
                        "operandType": "string",
                        "operator": "string",
                        "property": "string",
                        "then": "ComponentProperty"
                     },
                     "configured": boolean,
                     "defaultValue": "string",
                     "event": "string",
                     "importedValue": "string",
                     "model": "string",
                     "property": "string",
                     "type": "string",
                     "userAttribute": "string",
                     "value": "string"
                  },
                  "fields": {
                     "string" : {
                        "bindingProperties": {
                           "field": "string",
                           "property": "string"
                        },
                        "bindings": {
                           "string" : {
                              "element": "string",
                              "property": "string"
                           }
                        },
                        "collectionBindingProperties": {
                           "field": "string",
                           "property": "string"
                        },
                        "componentName": "string",
                        "concat": [
                           "ComponentProperty"
                        ],
                        "condition": {
                           "else": "ComponentProperty",
                           "field": "string",
                           "operand": "string",
                           "operandType": "string",
                           "operator": "string",
                           "property": "string",
                           "then": "ComponentProperty"
                        },
                        "configured": boolean,
                        "defaultValue": "string",
                        "event": "string",
                        "importedValue": "string",
                        "model": "string",
                        "property": "string",
                        "type": "string",
                        "userAttribute": "string",
                        "value": "string"
                     }
                  },
                  "global": {
                     "bindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "bindings": {
                        "string" : {
                           "element": "string",
                           "property": "string"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "componentName": "string",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "string",
                        "operand": "string",
                        "operandType": "string",
                        "operator": "string",
                        "property": "string",
                        "then": "ComponentProperty"
                     },
                     "configured": boolean,
                     "defaultValue": "string",
                     "event": "string",
                     "importedValue": "string",
                     "model": "string",
                     "property": "string",
                     "type": "string",
                     "userAttribute": "string",
                     "value": "string"
                  },
                  "id": {
                     "bindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "bindings": {
                        "string" : {
                           "element": "string",
                           "property": "string"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "componentName": "string",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "string",
                        "operand": "string",
                        "operandType": "string",
                        "operator": "string",
                        "property": "string",
                        "then": "ComponentProperty"
                     },
                     "configured": boolean,
                     "defaultValue": "string",
                     "event": "string",
                     "importedValue": "string",
                     "model": "string",
                     "property": "string",
                     "type": "string",
                     "userAttribute": "string",
                     "value": "string"
                  },
                  "model": "string",
                  "state": {
                     "componentName": "string",
                     "property": "string",
                     "set": {
                        "bindingProperties": {
                           "field": "string",
                           "property": "string"
                        },
                        "bindings": {
                           "string" : {
                              "element": "string",
                              "property": "string"
                           }
                        },
                        "collectionBindingProperties": {
                           "field": "string",
                           "property": "string"
                        },
                        "componentName": "string",
                        "concat": [
                           "ComponentProperty"
                        ],
                        "condition": {
                           "else": "ComponentProperty",
                           "field": "string",
                           "operand": "string",
                           "operandType": "string",
                           "operator": "string",
                           "property": "string",
                           "then": "ComponentProperty"
                        },
                        "configured": boolean,
                        "defaultValue": "string",
                        "event": "string",
                        "importedValue": "string",
                        "model": "string",
                        "property": "string",
                        "type": "string",
                        "userAttribute": "string",
                        "value": "string"
                     }
                  },
                  "target": {
                     "bindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "bindings": {
                        "string" : {
                           "element": "string",
                           "property": "string"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "componentName": "string",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "string",
                        "operand": "string",
                        "operandType": "string",
                        "operator": "string",
                        "property": "string",
                        "then": "ComponentProperty"
                     },
                     "configured": boolean,
                     "defaultValue": "string",
                     "event": "string",
                     "importedValue": "string",
                     "model": "string",
                     "property": "string",
                     "type": "string",
                     "userAttribute": "string",
                     "value": "string"
                  },
                  "type": {
                     "bindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "bindings": {
                        "string" : {
                           "element": "string",
                           "property": "string"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "componentName": "string",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "string",
                        "operand": "string",
                        "operandType": "string",
                        "operator": "string",
                        "property": "string",
                        "then": "ComponentProperty"
                     },
                     "configured": boolean,
                     "defaultValue": "string",
                     "event": "string",
                     "importedValue": "string",
                     "model": "string",
                     "property": "string",
                     "type": "string",
                     "userAttribute": "string",
                     "value": "string"
                  },
                  "url": {
                     "bindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "bindings": {
                        "string" : {
                           "element": "string",
                           "property": "string"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "string",
                        "property": "string"
                     },
                     "componentName": "string",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "string",
                        "operand": "string",
                        "operandType": "string",
                        "operator": "string",
                        "property": "string",
                        "then": "ComponentProperty"
                     },
                     "configured": boolean,
                     "defaultValue": "string",
                     "event": "string",
                     "importedValue": "string",
                     "model": "string",
                     "property": "string",
                     "type": "string",
                     "userAttribute": "string",
                     "value": "string"
                  }
               }
            }
         },
         "id": "string",
         "modifiedAt": "string",
         "name": "string",
         "overrides": {
            "string" : {
               "string" : "string"
            }
         },
         "properties": {
            "string" : {
               "bindingProperties": {
                  "field": "string",
                  "property": "string"
               },
               "bindings": {
                  "string" : {
                     "element": "string",
                     "property": "string"
                  }
               },
               "collectionBindingProperties": {
                  "field": "string",
                  "property": "string"
               },
               "componentName": "string",
               "concat": [
                  "ComponentProperty"
               ],
               "condition": {
                  "else": "ComponentProperty",
                  "field": "string",
                  "operand": "string",
                  "operandType": "string",
                  "operator": "string",
                  "property": "string",
                  "then": "ComponentProperty"
               },
               "configured": boolean,
               "defaultValue": "string",
               "event": "string",
               "importedValue": "string",
               "model": "string",
               "property": "string",
               "type": "string",
               "userAttribute": "string",
               "value": "string"
            }
         },
         "schemaVersion": "string",
         "sourceId": "string",
         "tags": {
            "string" : "string"
         },
         "variants": [
            {
               "overrides": {
                  "string" : {
                     "string" : "string"
                  }
               },
               "variantValues": {
                  "string" : "string"
               }
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ExportComponents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entities](#API_ExportComponents_ResponseSyntax) **   <a name="amplifyuibuilder-ExportComponents-response-entities"></a>
Represents the configuration of the exported components.
Type: Array of [Component](API_Component.md) objects

 ** [nextToken](#API_ExportComponents_ResponseSyntax) **   <a name="amplifyuibuilder-ExportComponents-response-nextToken"></a>
The pagination token that's included if more results are available.
Type: String

## Errors
<a name="API_ExportComponents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Please retry your request.
HTTP Status Code: 500

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ExportComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/ExportComponents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/ExportComponents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ExportComponents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/ExportComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ExportComponents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/ExportComponents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/ExportComponents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/ExportComponents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/ExportComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ExportComponents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
