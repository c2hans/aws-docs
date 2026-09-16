---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetEntity.html
---

# GetEntity
<a name="API_GetEntity"></a>

Retrieves information about an entity.

## Request Syntax
<a name="API_GetEntity_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/entities/{{entityId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEntity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [entityId](#API_GetEntity_RequestSyntax) **   <a name="tm-GetEntity-request-uri-entityId"></a>
The ID of the entity.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: Yes

 ** [workspaceId](#API_GetEntity_RequestSyntax) **   <a name="tm-GetEntity-request-uri-workspaceId"></a>
The ID of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_GetEntity_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEntity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "areAllComponentsReturned": boolean,
   "arn": "string",
   "components": {
      "string" : {
         "areAllCompositeComponentsReturned": boolean,
         "areAllPropertiesReturned": boolean,
         "componentName": "string",
         "componentTypeId": "string",
         "compositeComponents": {
            "string" : {
               "componentName": "string",
               "componentPath": "string",
               "componentTypeId": "string",
               "definedIn": "string",
               "description": "string",
               "propertyGroups": {
                  "string" : {
                     "groupType": "string",
                     "isInherited": boolean,
                     "propertyNames": [ "string" ]
                  }
               },
               "status": {
                  "error": {
                     "code": "string",
                     "message": "string"
                  },
                  "state": "string"
               },
               "syncSource": "string"
            }
         },
         "definedIn": "string",
         "description": "string",
         "properties": {
            "string" : {
               "areAllPropertyValuesReturned": boolean,
               "definition": {
                  "configuration": {
                     "string" : "string"
                  },
                  "dataType": {
                     "allowedValues": [
                        {
                           "booleanValue": boolean,
                           "doubleValue": number,
                           "expression": "string",
                           "integerValue": number,
                           "listValue": [
                              "DataValue"
                           ],
                           "longValue": number,
                           "mapValue": {
                              "string" : "DataValue"
                           },
                           "relationshipValue": {
                              "targetComponentName": "string",
                              "targetEntityId": "string"
                           },
                           "stringValue": "string"
                        }
                     ],
                     "nestedType": "DataType",
                     "relationship": {
                        "relationshipType": "string",
                        "targetComponentTypeId": "string"
                     },
                     "type": "string",
                     "unitOfMeasure": "string"
                  },
                  "defaultValue": {
                     "booleanValue": boolean,
                     "doubleValue": number,
                     "expression": "string",
                     "integerValue": number,
                     "listValue": [
                        "DataValue"
                     ],
                     "longValue": number,
                     "mapValue": {
                        "string" : "DataValue"
                     },
                     "relationshipValue": {
                        "targetComponentName": "string",
                        "targetEntityId": "string"
                     },
                     "stringValue": "string"
                  },
                  "displayName": "string",
                  "isExternalId": boolean,
                  "isFinal": boolean,
                  "isImported": boolean,
                  "isInherited": boolean,
                  "isRequiredInEntity": boolean,
                  "isStoredExternally": boolean,
                  "isTimeSeries": boolean
               },
               "value": {
                  "booleanValue": boolean,
                  "doubleValue": number,
                  "expression": "string",
                  "integerValue": number,
                  "listValue": [
                     "DataValue"
                  ],
                  "longValue": number,
                  "mapValue": {
                     "string" : "DataValue"
                  },
                  "relationshipValue": {
                     "targetComponentName": "string",
                     "targetEntityId": "string"
                  },
                  "stringValue": "string"
               }
            }
         },
         "propertyGroups": {
            "string" : {
               "groupType": "string",
               "isInherited": boolean,
               "propertyNames": [ "string" ]
            }
         },
         "status": {
            "error": {
               "code": "string",
               "message": "string"
            },
            "state": "string"
         },
         "syncSource": "string"
      }
   },
   "creationDateTime": number,
   "description": "string",
   "entityId": "string",
   "entityName": "string",
   "hasChildEntities": boolean,
   "parentEntityId": "string",
   "status": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   },
   "syncSource": "string",
   "updateDateTime": number,
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_GetEntity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [areAllComponentsReturned](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-areAllComponentsReturned"></a>
This flag notes whether all components are returned in the API response. The maximum number of components returned is 30.
Type: Boolean

 ** [arn](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-arn"></a>
The ARN of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [components](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-components"></a>
An object that maps strings to the components in the entity. Each string in the mapping must be unique to this object.
Type: String to [ComponentResponse](API_ComponentResponse.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`

 ** [creationDateTime](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-creationDateTime"></a>
The date and time when the entity was created.
Type: Timestamp

 ** [description](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-description"></a>
The description of the entity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

 ** [entityId](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-entityId"></a>
The ID of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`

 ** [entityName](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-entityName"></a>
The name of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [hasChildEntities](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-hasChildEntities"></a>
A Boolean value that specifies whether the entity has associated child entities.
Type: Boolean

 ** [parentEntityId](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-parentEntityId"></a>
The ID of the parent entity for this entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$ROOT|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`

 ** [status](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-status"></a>
The current status of the entity.
Type: [Status](API_Status.md) object

 ** [syncSource](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-syncSource"></a>
The syncSource of the sync job, if this entity was created by a sync job.
Type: String
Pattern: `[a-zA-Z_0-9]+`

 ** [updateDateTime](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-updateDateTime"></a>
The date and time when the entity was last updated.
Type: Timestamp

 ** [workspaceId](#API_GetEntity_ResponseSyntax) **   <a name="tm-GetEntity-response-workspaceId"></a>
The ID of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

## Errors
<a name="API_GetEntity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/GetEntity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/GetEntity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/GetEntity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/GetEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/GetEntity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/GetEntity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/GetEntity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/GetEntity)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/GetEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/GetEntity)
