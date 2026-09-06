---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_CreateEntity.html
---

# CreateEntity
<a name="API_CreateEntity"></a>

Creates an entity.

## Request Syntax
<a name="API_CreateEntity_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/entities HTTP/1.1
Content-type: application/json

{
   "components": {
      "{{string}}" : {
         "componentTypeId": "{{string}}",
         "description": "{{string}}",
         "properties": {
            "{{string}}" : {
               "definition": {
                  "configuration": {
                     "{{string}}" : "{{string}}"
                  },
                  "dataType": {
                     "allowedValues": [
                        {
                           "booleanValue": {{boolean}},
                           "doubleValue": {{number}},
                           "expression": "{{string}}",
                           "integerValue": {{number}},
                           "listValue": [
                              "DataValue"
                           ],
                           "longValue": {{number}},
                           "mapValue": {
                              "{{string}}" : "DataValue"
                           },
                           "relationshipValue": {
                              "targetComponentName": "{{string}}",
                              "targetEntityId": "{{string}}"
                           },
                           "stringValue": "{{string}}"
                        }
                     ],
                     "nestedType": "DataType",
                     "relationship": {
                        "relationshipType": "{{string}}",
                        "targetComponentTypeId": "{{string}}"
                     },
                     "type": "{{string}}",
                     "unitOfMeasure": "{{string}}"
                  },
                  "defaultValue": {
                     "booleanValue": {{boolean}},
                     "doubleValue": {{number}},
                     "expression": "{{string}}",
                     "integerValue": {{number}},
                     "listValue": [
                        "DataValue"
                     ],
                     "longValue": {{number}},
                     "mapValue": {
                        "{{string}}" : "DataValue"
                     },
                     "relationshipValue": {
                        "targetComponentName": "{{string}}",
                        "targetEntityId": "{{string}}"
                     },
                     "stringValue": "{{string}}"
                  },
                  "displayName": "{{string}}",
                  "isExternalId": {{boolean}},
                  "isRequiredInEntity": {{boolean}},
                  "isStoredExternally": {{boolean}},
                  "isTimeSeries": {{boolean}}
               },
               "updateType": "{{string}}",
               "value": {
                  "booleanValue": {{boolean}},
                  "doubleValue": {{number}},
                  "expression": "{{string}}",
                  "integerValue": {{number}},
                  "listValue": [
                     "DataValue"
                  ],
                  "longValue": {{number}},
                  "mapValue": {
                     "{{string}}" : "DataValue"
                  },
                  "relationshipValue": {
                     "targetComponentName": "{{string}}",
                     "targetEntityId": "{{string}}"
                  },
                  "stringValue": "{{string}}"
               }
            }
         },
         "propertyGroups": {
            "{{string}}" : {
               "groupType": "{{string}}",
               "propertyNames": [ "{{string}}" ],
               "updateType": "{{string}}"
            }
         }
      }
   },
   "compositeComponents": {
      "{{string}}" : {
         "description": "{{string}}",
         "properties": {
            "{{string}}" : {
               "definition": {
                  "configuration": {
                     "{{string}}" : "{{string}}"
                  },
                  "dataType": {
                     "allowedValues": [
                        {
                           "booleanValue": {{boolean}},
                           "doubleValue": {{number}},
                           "expression": "{{string}}",
                           "integerValue": {{number}},
                           "listValue": [
                              "DataValue"
                           ],
                           "longValue": {{number}},
                           "mapValue": {
                              "{{string}}" : "DataValue"
                           },
                           "relationshipValue": {
                              "targetComponentName": "{{string}}",
                              "targetEntityId": "{{string}}"
                           },
                           "stringValue": "{{string}}"
                        }
                     ],
                     "nestedType": "DataType",
                     "relationship": {
                        "relationshipType": "{{string}}",
                        "targetComponentTypeId": "{{string}}"
                     },
                     "type": "{{string}}",
                     "unitOfMeasure": "{{string}}"
                  },
                  "defaultValue": {
                     "booleanValue": {{boolean}},
                     "doubleValue": {{number}},
                     "expression": "{{string}}",
                     "integerValue": {{number}},
                     "listValue": [
                        "DataValue"
                     ],
                     "longValue": {{number}},
                     "mapValue": {
                        "{{string}}" : "DataValue"
                     },
                     "relationshipValue": {
                        "targetComponentName": "{{string}}",
                        "targetEntityId": "{{string}}"
                     },
                     "stringValue": "{{string}}"
                  },
                  "displayName": "{{string}}",
                  "isExternalId": {{boolean}},
                  "isRequiredInEntity": {{boolean}},
                  "isStoredExternally": {{boolean}},
                  "isTimeSeries": {{boolean}}
               },
               "updateType": "{{string}}",
               "value": {
                  "booleanValue": {{boolean}},
                  "doubleValue": {{number}},
                  "expression": "{{string}}",
                  "integerValue": {{number}},
                  "listValue": [
                     "DataValue"
                  ],
                  "longValue": {{number}},
                  "mapValue": {
                     "{{string}}" : "DataValue"
                  },
                  "relationshipValue": {
                     "targetComponentName": "{{string}}",
                     "targetEntityId": "{{string}}"
                  },
                  "stringValue": "{{string}}"
               }
            }
         },
         "propertyGroups": {
            "{{string}}" : {
               "groupType": "{{string}}",
               "propertyNames": [ "{{string}}" ],
               "updateType": "{{string}}"
            }
         }
      }
   },
   "description": "{{string}}",
   "entityId": "{{string}}",
   "entityName": "{{string}}",
   "parentEntityId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEntity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_CreateEntity_RequestSyntax) **   <a name="tm-CreateEntity-request-uri-workspaceId"></a>
The ID of the workspace that contains the entity.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_CreateEntity_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [components](#API_CreateEntity_RequestSyntax) **   <a name="tm-CreateEntity-request-components"></a>
An object that maps strings to the components in the entity. Each string in the mapping must be unique to this object.
Type: String to [ComponentRequest](API_ComponentRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** [compositeComponents](#API_CreateEntity_RequestSyntax) **   <a name="tm-CreateEntity-request-compositeComponents"></a>
This is an object that maps strings to `compositeComponent` updates in the request. Each key of the map represents the `componentPath` of the `compositeComponent`.
Type: String to [CompositeComponentRequest](API_CompositeComponentRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Key Pattern: `[a-zA-Z_\-0-9/]+`
Required: No

 ** [description](#API_CreateEntity_RequestSyntax) **   <a name="tm-CreateEntity-request-description"></a>
The description of the entity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [entityId](#API_CreateEntity_RequestSyntax) **   <a name="tm-CreateEntity-request-entityId"></a>
The ID of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: No

 ** [entityName](#API_CreateEntity_RequestSyntax) **   <a name="tm-CreateEntity-request-entityName"></a>
The name of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [parentEntityId](#API_CreateEntity_RequestSyntax) **   <a name="tm-CreateEntity-request-parentEntityId"></a>
The ID of the entity's parent entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$ROOT|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: No

 ** [tags](#API_CreateEntity_RequestSyntax) **   <a name="tm-CreateEntity-request-tags"></a>
Metadata that you can use to manage the entity.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `.*`
Required: No

## Response Syntax
<a name="API_CreateEntity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationDateTime": number,
   "entityId": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_CreateEntity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateEntity_ResponseSyntax) **   <a name="tm-CreateEntity-response-arn"></a>
The ARN of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [creationDateTime](#API_CreateEntity_ResponseSyntax) **   <a name="tm-CreateEntity-response-creationDateTime"></a>
The date and time when the entity was created.
Type: Timestamp

 ** [entityId](#API_CreateEntity_ResponseSyntax) **   <a name="tm-CreateEntity-response-entityId"></a>
The ID of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`

 ** [state](#API_CreateEntity_ResponseSyntax) **   <a name="tm-CreateEntity-response-state"></a>
The current state of the entity.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | ERROR`

## Errors
<a name="API_CreateEntity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The service quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_CreateEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/CreateEntity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/CreateEntity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/CreateEntity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/CreateEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/CreateEntity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/CreateEntity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/CreateEntity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/CreateEntity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/CreateEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/CreateEntity)
