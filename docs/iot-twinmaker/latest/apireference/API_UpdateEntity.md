---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdateEntity.html
---

# UpdateEntity
<a name="API_UpdateEntity"></a>

Updates an entity.

## Request Syntax
<a name="API_UpdateEntity_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}}/entities/{{entityId}} HTTP/1.1
Content-type: application/json

{
   "componentUpdates": {
      "{{string}}" : {
         "componentTypeId": "{{string}}",
         "description": "{{string}}",
         "propertyGroupUpdates": {
            "{{string}}" : {
               "groupType": "{{string}}",
               "propertyNames": [ "{{string}}" ],
               "updateType": "{{string}}"
            }
         },
         "propertyUpdates": {
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
         "updateType": "{{string}}"
      }
   },
   "compositeComponentUpdates": {
      "{{string}}" : {
         "description": "{{string}}",
         "propertyGroupUpdates": {
            "{{string}}" : {
               "groupType": "{{string}}",
               "propertyNames": [ "{{string}}" ],
               "updateType": "{{string}}"
            }
         },
         "propertyUpdates": {
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
         "updateType": "{{string}}"
      }
   },
   "description": "{{string}}",
   "entityName": "{{string}}",
   "parentEntityUpdate": {
      "parentEntityId": "{{string}}",
      "updateType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateEntity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [entityId](#API_UpdateEntity_RequestSyntax) **   <a name="tm-UpdateEntity-request-uri-entityId"></a>
The ID of the entity.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: Yes

 ** [workspaceId](#API_UpdateEntity_RequestSyntax) **   <a name="tm-UpdateEntity-request-uri-workspaceId"></a>
The ID of the workspace that contains the entity.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateEntity_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [componentUpdates](#API_UpdateEntity_RequestSyntax) **   <a name="tm-UpdateEntity-request-componentUpdates"></a>
An object that maps strings to the component updates in the request. Each string in the mapping must be unique to this object.
Type: String to [ComponentUpdateRequest](API_ComponentUpdateRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** [compositeComponentUpdates](#API_UpdateEntity_RequestSyntax) **   <a name="tm-UpdateEntity-request-compositeComponentUpdates"></a>
This is an object that maps strings to `compositeComponent` updates in the request. Each key of the map represents the `componentPath` of the `compositeComponent`.
Type: String to [CompositeComponentUpdateRequest](API_CompositeComponentUpdateRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Key Pattern: `[a-zA-Z_\-0-9/]+`
Required: No

 ** [description](#API_UpdateEntity_RequestSyntax) **   <a name="tm-UpdateEntity-request-description"></a>
The description of the entity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [entityName](#API_UpdateEntity_RequestSyntax) **   <a name="tm-UpdateEntity-request-entityName"></a>
The name of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [parentEntityUpdate](#API_UpdateEntity_RequestSyntax) **   <a name="tm-UpdateEntity-request-parentEntityUpdate"></a>
An object that describes the update request for a parent entity.
Type: [ParentEntityUpdateRequest](API_ParentEntityUpdateRequest.md) object
Required: No

## Response Syntax
<a name="API_UpdateEntity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "state": "string",
   "updateDateTime": number
}
```

## Response Elements
<a name="API_UpdateEntity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [state](#API_UpdateEntity_ResponseSyntax) **   <a name="tm-UpdateEntity-response-state"></a>
The current state of the entity update.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | ERROR`

 ** [updateDateTime](#API_UpdateEntity_ResponseSyntax) **   <a name="tm-UpdateEntity-response-updateDateTime"></a>
The date and time when the entity was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateEntity_Errors"></a>

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

 ** ResourceNotFoundException **
The resource wasn't found.
HTTP Status Code: 404

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
<a name="API_UpdateEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/UpdateEntity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/UpdateEntity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/UpdateEntity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/UpdateEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/UpdateEntity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/UpdateEntity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/UpdateEntity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/UpdateEntity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/UpdateEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/UpdateEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
