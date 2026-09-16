---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateComponent.html
---

# UpdateComponent
<a name="API_UpdateComponent"></a>

Updates an existing component.

## Request Syntax
<a name="API_UpdateComponent_RequestSyntax"></a>

```
PATCH /app/{{appId}}/environment/{{environmentName}}/components/{{id}}?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "bindingProperties": {
      "{{string}}" : {
         "bindingProperties": {
            "bucket": "{{string}}",
            "defaultValue": "{{string}}",
            "field": "{{string}}",
            "key": "{{string}}",
            "model": "{{string}}",
            "predicates": [
               {
                  "and": [
                     "Predicate"
                  ],
                  "field": "{{string}}",
                  "operand": "{{string}}",
                  "operandType": "{{string}}",
                  "operator": "{{string}}",
                  "or": [
                     "Predicate"
                  ]
               }
            ],
            "slotName": "{{string}}",
            "userAttribute": "{{string}}"
         },
         "defaultValue": "{{string}}",
         "type": "{{string}}"
      }
   },
   "children": [
      {
         "children": [
            "ComponentChild"
         ],
         "componentType": "{{string}}",
         "events": {
            "{{string}}" : {
               "action": "{{string}}",
               "bindingEvent": "{{string}}",
               "parameters": {
                  "anchor": {
                     "bindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "bindings": {
                        "{{string}}" : {
                           "element": "{{string}}",
                           "property": "{{string}}"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "componentName": "{{string}}",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "{{string}}",
                        "operand": "{{string}}",
                        "operandType": "{{string}}",
                        "operator": "{{string}}",
                        "property": "{{string}}",
                        "then": "ComponentProperty"
                     },
                     "configured": {{boolean}},
                     "defaultValue": "{{string}}",
                     "event": "{{string}}",
                     "importedValue": "{{string}}",
                     "model": "{{string}}",
                     "property": "{{string}}",
                     "type": "{{string}}",
                     "userAttribute": "{{string}}",
                     "value": "{{string}}"
                  },
                  "fields": {
                     "{{string}}" : {
                        "bindingProperties": {
                           "field": "{{string}}",
                           "property": "{{string}}"
                        },
                        "bindings": {
                           "{{string}}" : {
                              "element": "{{string}}",
                              "property": "{{string}}"
                           }
                        },
                        "collectionBindingProperties": {
                           "field": "{{string}}",
                           "property": "{{string}}"
                        },
                        "componentName": "{{string}}",
                        "concat": [
                           "ComponentProperty"
                        ],
                        "condition": {
                           "else": "ComponentProperty",
                           "field": "{{string}}",
                           "operand": "{{string}}",
                           "operandType": "{{string}}",
                           "operator": "{{string}}",
                           "property": "{{string}}",
                           "then": "ComponentProperty"
                        },
                        "configured": {{boolean}},
                        "defaultValue": "{{string}}",
                        "event": "{{string}}",
                        "importedValue": "{{string}}",
                        "model": "{{string}}",
                        "property": "{{string}}",
                        "type": "{{string}}",
                        "userAttribute": "{{string}}",
                        "value": "{{string}}"
                     }
                  },
                  "global": {
                     "bindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "bindings": {
                        "{{string}}" : {
                           "element": "{{string}}",
                           "property": "{{string}}"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "componentName": "{{string}}",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "{{string}}",
                        "operand": "{{string}}",
                        "operandType": "{{string}}",
                        "operator": "{{string}}",
                        "property": "{{string}}",
                        "then": "ComponentProperty"
                     },
                     "configured": {{boolean}},
                     "defaultValue": "{{string}}",
                     "event": "{{string}}",
                     "importedValue": "{{string}}",
                     "model": "{{string}}",
                     "property": "{{string}}",
                     "type": "{{string}}",
                     "userAttribute": "{{string}}",
                     "value": "{{string}}"
                  },
                  "id": {
                     "bindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "bindings": {
                        "{{string}}" : {
                           "element": "{{string}}",
                           "property": "{{string}}"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "componentName": "{{string}}",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "{{string}}",
                        "operand": "{{string}}",
                        "operandType": "{{string}}",
                        "operator": "{{string}}",
                        "property": "{{string}}",
                        "then": "ComponentProperty"
                     },
                     "configured": {{boolean}},
                     "defaultValue": "{{string}}",
                     "event": "{{string}}",
                     "importedValue": "{{string}}",
                     "model": "{{string}}",
                     "property": "{{string}}",
                     "type": "{{string}}",
                     "userAttribute": "{{string}}",
                     "value": "{{string}}"
                  },
                  "model": "{{string}}",
                  "state": {
                     "componentName": "{{string}}",
                     "property": "{{string}}",
                     "set": {
                        "bindingProperties": {
                           "field": "{{string}}",
                           "property": "{{string}}"
                        },
                        "bindings": {
                           "{{string}}" : {
                              "element": "{{string}}",
                              "property": "{{string}}"
                           }
                        },
                        "collectionBindingProperties": {
                           "field": "{{string}}",
                           "property": "{{string}}"
                        },
                        "componentName": "{{string}}",
                        "concat": [
                           "ComponentProperty"
                        ],
                        "condition": {
                           "else": "ComponentProperty",
                           "field": "{{string}}",
                           "operand": "{{string}}",
                           "operandType": "{{string}}",
                           "operator": "{{string}}",
                           "property": "{{string}}",
                           "then": "ComponentProperty"
                        },
                        "configured": {{boolean}},
                        "defaultValue": "{{string}}",
                        "event": "{{string}}",
                        "importedValue": "{{string}}",
                        "model": "{{string}}",
                        "property": "{{string}}",
                        "type": "{{string}}",
                        "userAttribute": "{{string}}",
                        "value": "{{string}}"
                     }
                  },
                  "target": {
                     "bindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "bindings": {
                        "{{string}}" : {
                           "element": "{{string}}",
                           "property": "{{string}}"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "componentName": "{{string}}",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "{{string}}",
                        "operand": "{{string}}",
                        "operandType": "{{string}}",
                        "operator": "{{string}}",
                        "property": "{{string}}",
                        "then": "ComponentProperty"
                     },
                     "configured": {{boolean}},
                     "defaultValue": "{{string}}",
                     "event": "{{string}}",
                     "importedValue": "{{string}}",
                     "model": "{{string}}",
                     "property": "{{string}}",
                     "type": "{{string}}",
                     "userAttribute": "{{string}}",
                     "value": "{{string}}"
                  },
                  "type": {
                     "bindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "bindings": {
                        "{{string}}" : {
                           "element": "{{string}}",
                           "property": "{{string}}"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "componentName": "{{string}}",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "{{string}}",
                        "operand": "{{string}}",
                        "operandType": "{{string}}",
                        "operator": "{{string}}",
                        "property": "{{string}}",
                        "then": "ComponentProperty"
                     },
                     "configured": {{boolean}},
                     "defaultValue": "{{string}}",
                     "event": "{{string}}",
                     "importedValue": "{{string}}",
                     "model": "{{string}}",
                     "property": "{{string}}",
                     "type": "{{string}}",
                     "userAttribute": "{{string}}",
                     "value": "{{string}}"
                  },
                  "url": {
                     "bindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "bindings": {
                        "{{string}}" : {
                           "element": "{{string}}",
                           "property": "{{string}}"
                        }
                     },
                     "collectionBindingProperties": {
                        "field": "{{string}}",
                        "property": "{{string}}"
                     },
                     "componentName": "{{string}}",
                     "concat": [
                        "ComponentProperty"
                     ],
                     "condition": {
                        "else": "ComponentProperty",
                        "field": "{{string}}",
                        "operand": "{{string}}",
                        "operandType": "{{string}}",
                        "operator": "{{string}}",
                        "property": "{{string}}",
                        "then": "ComponentProperty"
                     },
                     "configured": {{boolean}},
                     "defaultValue": "{{string}}",
                     "event": "{{string}}",
                     "importedValue": "{{string}}",
                     "model": "{{string}}",
                     "property": "{{string}}",
                     "type": "{{string}}",
                     "userAttribute": "{{string}}",
                     "value": "{{string}}"
                  }
               }
            }
         },
         "name": "{{string}}",
         "properties": {
            "{{string}}" : {
               "bindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "bindings": {
                  "{{string}}" : {
                     "element": "{{string}}",
                     "property": "{{string}}"
                  }
               },
               "collectionBindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "componentName": "{{string}}",
               "concat": [
                  "ComponentProperty"
               ],
               "condition": {
                  "else": "ComponentProperty",
                  "field": "{{string}}",
                  "operand": "{{string}}",
                  "operandType": "{{string}}",
                  "operator": "{{string}}",
                  "property": "{{string}}",
                  "then": "ComponentProperty"
               },
               "configured": {{boolean}},
               "defaultValue": "{{string}}",
               "event": "{{string}}",
               "importedValue": "{{string}}",
               "model": "{{string}}",
               "property": "{{string}}",
               "type": "{{string}}",
               "userAttribute": "{{string}}",
               "value": "{{string}}"
            }
         },
         "sourceId": "{{string}}"
      }
   ],
   "collectionProperties": {
      "{{string}}" : {
         "identifiers": [ "{{string}}" ],
         "model": "{{string}}",
         "predicate": {
            "and": [
               "Predicate"
            ],
            "field": "{{string}}",
            "operand": "{{string}}",
            "operandType": "{{string}}",
            "operator": "{{string}}",
            "or": [
               "Predicate"
            ]
         },
         "sort": [
            {
               "direction": "{{string}}",
               "field": "{{string}}"
            }
         ]
      }
   },
   "componentType": "{{string}}",
   "events": {
      "{{string}}" : {
         "action": "{{string}}",
         "bindingEvent": "{{string}}",
         "parameters": {
            "anchor": {
               "bindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "bindings": {
                  "{{string}}" : {
                     "element": "{{string}}",
                     "property": "{{string}}"
                  }
               },
               "collectionBindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "componentName": "{{string}}",
               "concat": [
                  "ComponentProperty"
               ],
               "condition": {
                  "else": "ComponentProperty",
                  "field": "{{string}}",
                  "operand": "{{string}}",
                  "operandType": "{{string}}",
                  "operator": "{{string}}",
                  "property": "{{string}}",
                  "then": "ComponentProperty"
               },
               "configured": {{boolean}},
               "defaultValue": "{{string}}",
               "event": "{{string}}",
               "importedValue": "{{string}}",
               "model": "{{string}}",
               "property": "{{string}}",
               "type": "{{string}}",
               "userAttribute": "{{string}}",
               "value": "{{string}}"
            },
            "fields": {
               "{{string}}" : {
                  "bindingProperties": {
                     "field": "{{string}}",
                     "property": "{{string}}"
                  },
                  "bindings": {
                     "{{string}}" : {
                        "element": "{{string}}",
                        "property": "{{string}}"
                     }
                  },
                  "collectionBindingProperties": {
                     "field": "{{string}}",
                     "property": "{{string}}"
                  },
                  "componentName": "{{string}}",
                  "concat": [
                     "ComponentProperty"
                  ],
                  "condition": {
                     "else": "ComponentProperty",
                     "field": "{{string}}",
                     "operand": "{{string}}",
                     "operandType": "{{string}}",
                     "operator": "{{string}}",
                     "property": "{{string}}",
                     "then": "ComponentProperty"
                  },
                  "configured": {{boolean}},
                  "defaultValue": "{{string}}",
                  "event": "{{string}}",
                  "importedValue": "{{string}}",
                  "model": "{{string}}",
                  "property": "{{string}}",
                  "type": "{{string}}",
                  "userAttribute": "{{string}}",
                  "value": "{{string}}"
               }
            },
            "global": {
               "bindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "bindings": {
                  "{{string}}" : {
                     "element": "{{string}}",
                     "property": "{{string}}"
                  }
               },
               "collectionBindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "componentName": "{{string}}",
               "concat": [
                  "ComponentProperty"
               ],
               "condition": {
                  "else": "ComponentProperty",
                  "field": "{{string}}",
                  "operand": "{{string}}",
                  "operandType": "{{string}}",
                  "operator": "{{string}}",
                  "property": "{{string}}",
                  "then": "ComponentProperty"
               },
               "configured": {{boolean}},
               "defaultValue": "{{string}}",
               "event": "{{string}}",
               "importedValue": "{{string}}",
               "model": "{{string}}",
               "property": "{{string}}",
               "type": "{{string}}",
               "userAttribute": "{{string}}",
               "value": "{{string}}"
            },
            "id": {
               "bindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "bindings": {
                  "{{string}}" : {
                     "element": "{{string}}",
                     "property": "{{string}}"
                  }
               },
               "collectionBindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "componentName": "{{string}}",
               "concat": [
                  "ComponentProperty"
               ],
               "condition": {
                  "else": "ComponentProperty",
                  "field": "{{string}}",
                  "operand": "{{string}}",
                  "operandType": "{{string}}",
                  "operator": "{{string}}",
                  "property": "{{string}}",
                  "then": "ComponentProperty"
               },
               "configured": {{boolean}},
               "defaultValue": "{{string}}",
               "event": "{{string}}",
               "importedValue": "{{string}}",
               "model": "{{string}}",
               "property": "{{string}}",
               "type": "{{string}}",
               "userAttribute": "{{string}}",
               "value": "{{string}}"
            },
            "model": "{{string}}",
            "state": {
               "componentName": "{{string}}",
               "property": "{{string}}",
               "set": {
                  "bindingProperties": {
                     "field": "{{string}}",
                     "property": "{{string}}"
                  },
                  "bindings": {
                     "{{string}}" : {
                        "element": "{{string}}",
                        "property": "{{string}}"
                     }
                  },
                  "collectionBindingProperties": {
                     "field": "{{string}}",
                     "property": "{{string}}"
                  },
                  "componentName": "{{string}}",
                  "concat": [
                     "ComponentProperty"
                  ],
                  "condition": {
                     "else": "ComponentProperty",
                     "field": "{{string}}",
                     "operand": "{{string}}",
                     "operandType": "{{string}}",
                     "operator": "{{string}}",
                     "property": "{{string}}",
                     "then": "ComponentProperty"
                  },
                  "configured": {{boolean}},
                  "defaultValue": "{{string}}",
                  "event": "{{string}}",
                  "importedValue": "{{string}}",
                  "model": "{{string}}",
                  "property": "{{string}}",
                  "type": "{{string}}",
                  "userAttribute": "{{string}}",
                  "value": "{{string}}"
               }
            },
            "target": {
               "bindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "bindings": {
                  "{{string}}" : {
                     "element": "{{string}}",
                     "property": "{{string}}"
                  }
               },
               "collectionBindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "componentName": "{{string}}",
               "concat": [
                  "ComponentProperty"
               ],
               "condition": {
                  "else": "ComponentProperty",
                  "field": "{{string}}",
                  "operand": "{{string}}",
                  "operandType": "{{string}}",
                  "operator": "{{string}}",
                  "property": "{{string}}",
                  "then": "ComponentProperty"
               },
               "configured": {{boolean}},
               "defaultValue": "{{string}}",
               "event": "{{string}}",
               "importedValue": "{{string}}",
               "model": "{{string}}",
               "property": "{{string}}",
               "type": "{{string}}",
               "userAttribute": "{{string}}",
               "value": "{{string}}"
            },
            "type": {
               "bindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "bindings": {
                  "{{string}}" : {
                     "element": "{{string}}",
                     "property": "{{string}}"
                  }
               },
               "collectionBindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "componentName": "{{string}}",
               "concat": [
                  "ComponentProperty"
               ],
               "condition": {
                  "else": "ComponentProperty",
                  "field": "{{string}}",
                  "operand": "{{string}}",
                  "operandType": "{{string}}",
                  "operator": "{{string}}",
                  "property": "{{string}}",
                  "then": "ComponentProperty"
               },
               "configured": {{boolean}},
               "defaultValue": "{{string}}",
               "event": "{{string}}",
               "importedValue": "{{string}}",
               "model": "{{string}}",
               "property": "{{string}}",
               "type": "{{string}}",
               "userAttribute": "{{string}}",
               "value": "{{string}}"
            },
            "url": {
               "bindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "bindings": {
                  "{{string}}" : {
                     "element": "{{string}}",
                     "property": "{{string}}"
                  }
               },
               "collectionBindingProperties": {
                  "field": "{{string}}",
                  "property": "{{string}}"
               },
               "componentName": "{{string}}",
               "concat": [
                  "ComponentProperty"
               ],
               "condition": {
                  "else": "ComponentProperty",
                  "field": "{{string}}",
                  "operand": "{{string}}",
                  "operandType": "{{string}}",
                  "operator": "{{string}}",
                  "property": "{{string}}",
                  "then": "ComponentProperty"
               },
               "configured": {{boolean}},
               "defaultValue": "{{string}}",
               "event": "{{string}}",
               "importedValue": "{{string}}",
               "model": "{{string}}",
               "property": "{{string}}",
               "type": "{{string}}",
               "userAttribute": "{{string}}",
               "value": "{{string}}"
            }
         }
      }
   },
   "id": "{{string}}",
   "name": "{{string}}",
   "overrides": {
      "{{string}}" : {
         "{{string}}" : "{{string}}"
      }
   },
   "properties": {
      "{{string}}" : {
         "bindingProperties": {
            "field": "{{string}}",
            "property": "{{string}}"
         },
         "bindings": {
            "{{string}}" : {
               "element": "{{string}}",
               "property": "{{string}}"
            }
         },
         "collectionBindingProperties": {
            "field": "{{string}}",
            "property": "{{string}}"
         },
         "componentName": "{{string}}",
         "concat": [
            "ComponentProperty"
         ],
         "condition": {
            "else": "ComponentProperty",
            "field": "{{string}}",
            "operand": "{{string}}",
            "operandType": "{{string}}",
            "operator": "{{string}}",
            "property": "{{string}}",
            "then": "ComponentProperty"
         },
         "configured": {{boolean}},
         "defaultValue": "{{string}}",
         "event": "{{string}}",
         "importedValue": "{{string}}",
         "model": "{{string}}",
         "property": "{{string}}",
         "type": "{{string}}",
         "userAttribute": "{{string}}",
         "value": "{{string}}"
      }
   },
   "schemaVersion": "{{string}}",
   "sourceId": "{{string}}",
   "variants": [
      {
         "overrides": {
            "{{string}}" : {
               "{{string}}" : "{{string}}"
            }
         },
         "variantValues": {
            "{{string}}" : "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateComponent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-uri-appId"></a>
The unique ID for the Amplify app.
Required: Yes

 ** [clientToken](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-uri-clientToken"></a>
The unique client token.

 ** [environmentName](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-uri-environmentName"></a>
The name of the backend environment that is part of the Amplify app.
Required: Yes

 ** [id](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-uri-id"></a>
The unique ID for the component.
Required: Yes

## Request Body
<a name="API_UpdateComponent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [bindingProperties](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-bindingProperties"></a>
The data binding information for the component's properties.
Type: String to [ComponentBindingPropertiesValue](API_ComponentBindingPropertiesValue.md) object map
Required: No

 ** [children](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-children"></a>
The components that are instances of the main component.
Type: Array of [ComponentChild](API_ComponentChild.md) objects
Required: No

 ** [collectionProperties](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-collectionProperties"></a>
The configuration for binding a component's properties to a data model. Use this for a collection component.
Type: String to [ComponentDataConfiguration](API_ComponentDataConfiguration.md) object map
Required: No

 ** [componentType](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-componentType"></a>
The type of the component. This can be an Amplify custom UI component or another custom component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [events](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-events"></a>
The event configuration for the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
Type: String to [ComponentEvent](API_ComponentEvent.md) object map
Required: No

 ** [id](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-id"></a>
The unique ID of the component to update.
Type: String
Required: No

 ** [name](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-name"></a>
The name of the component to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [overrides](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-overrides"></a>
Describes the properties that can be overriden to customize the component.
Type: String to string to string map map
Required: No

 ** [properties](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-properties"></a>
Describes the component's properties.
Type: String to [ComponentProperty](API_ComponentProperty.md) object map
Required: No

 ** [schemaVersion](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-schemaVersion"></a>
The schema version of the component when it was imported.
Type: String
Required: No

 ** [sourceId](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-sourceId"></a>
The unique ID of the component in its original source system, such as Figma.
Type: String
Required: No

 ** [variants](#API_UpdateComponent_RequestSyntax) **   <a name="amplifyuibuilder-UpdateComponent-request-variants"></a>
A list of the unique variants of the main component being updated.
Type: Array of [ComponentVariant](API_ComponentVariant.md) objects
Required: No

## Response Syntax
<a name="API_UpdateComponent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_UpdateComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appId](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-appId"></a>
The unique ID of the Amplify app associated with the component.
Type: String

 ** [bindingProperties](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-bindingProperties"></a>
The information to connect a component's properties to data at runtime. You can't specify `tags` as a valid property for `bindingProperties`.

Type: String to [ComponentBindingPropertiesValue](API_ComponentBindingPropertiesValue.md) object map

 ** [children](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-children"></a>
A list of the component's `ComponentChild` instances.
Type: Array of [ComponentChild](API_ComponentChild.md) objects

 ** [collectionProperties](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-collectionProperties"></a>
The data binding configuration for the component's properties. Use this for a collection component. You can't specify `tags` as a valid property for `collectionProperties`.
Type: String to [ComponentDataConfiguration](API_ComponentDataConfiguration.md) object map

 ** [componentType](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-componentType"></a>
The type of the component. This can be an Amplify custom UI component or another custom component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [createdAt](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-createdAt"></a>
The time that the component was created.
Type: Timestamp

 ** [environmentName](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Type: String

 ** [events](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-events"></a>
Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
Type: String to [ComponentEvent](API_ComponentEvent.md) object map

 ** [id](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-id"></a>
The unique ID of the component.
Type: String

 ** [modifiedAt](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-modifiedAt"></a>
The time that the component was modified.
Type: Timestamp

 ** [name](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-name"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [overrides](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-overrides"></a>
Describes the component's properties that can be overriden in a customized instance of the component. You can't specify `tags` as a valid property for `overrides`.
Type: String to string to string map map

 ** [properties](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-properties"></a>
Describes the component's properties. You can't specify `tags` as a valid property for `properties`.
Type: String to [ComponentProperty](API_ComponentProperty.md) object map

 ** [schemaVersion](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-schemaVersion"></a>
The schema version of the component when it was imported.
Type: String

 ** [sourceId](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-sourceId"></a>
The unique ID of the component in its original source system, such as Figma.
Type: String

 ** [tags](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-tags"></a>
One or more key-value pairs to use when tagging the component.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [variants](#API_UpdateComponent_ResponseSyntax) **   <a name="amplifyuibuilder-UpdateComponent-response-variants"></a>
A list of the component's variants. A variant is a unique style configuration of a main component.
Type: Array of [ComponentVariant](API_ComponentVariant.md) objects

## Errors
<a name="API_UpdateComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Please retry your request.
HTTP Status Code: 500

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource specified in the request conflicts with an existing resource.
HTTP Status Code: 409

## See Also
<a name="API_UpdateComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/UpdateComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/UpdateComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/UpdateComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/UpdateComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/UpdateComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/UpdateComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/UpdateComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/UpdateComponent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/UpdateComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/UpdateComponent)
