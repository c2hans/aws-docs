---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetComponentType.html
---

# GetComponentType
<a name="API_GetComponentType"></a>

Retrieves information about a component type.

## Request Syntax
<a name="API_GetComponentType_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/component-types/{{componentTypeId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetComponentType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [componentTypeId](#API_GetComponentType_RequestSyntax) **   <a name="tm-GetComponentType-request-uri-componentTypeId"></a>
The ID of the component type.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: Yes

 ** [workspaceId](#API_GetComponentType_RequestSyntax) **   <a name="tm-GetComponentType-request-uri-workspaceId"></a>
The ID of the workspace that contains the component type.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_GetComponentType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetComponentType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "componentTypeId": "string",
   "componentTypeName": "string",
   "compositeComponentTypes": {
      "string" : {
         "componentTypeId": "string",
         "isInherited": boolean
      }
   },
   "creationDateTime": number,
   "description": "string",
   "extendsFrom": [ "string" ],
   "functions": {
      "string" : {
         "implementedBy": {
            "isNative": boolean,
            "lambda": {
               "arn": "string"
            }
         },
         "isInherited": boolean,
         "requiredProperties": [ "string" ],
         "scope": "string"
      }
   },
   "isAbstract": boolean,
   "isSchemaInitialized": boolean,
   "isSingleton": boolean,
   "propertyDefinitions": {
      "string" : {
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
   "syncSource": "string",
   "updateDateTime": number,
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_GetComponentType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-arn"></a>
The ARN of the component type.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [componentTypeId](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-componentTypeId"></a>
The ID of the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`

 ** [componentTypeName](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-componentTypeName"></a>
The component type name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*[^\u0000-\u001F\u007F]*.*`

 ** [compositeComponentTypes](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-compositeComponentTypes"></a>
This is an object that maps strings to `compositeComponentTypes` of the `componentType`. `CompositeComponentType` is referenced by `componentTypeId`.
Type: String to [CompositeComponentTypeResponse](API_CompositeComponentTypeResponse.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`

 ** [creationDateTime](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-creationDateTime"></a>
The date and time when the component type was created.
Type: Timestamp

 ** [description](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-description"></a>
The description of the component type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

 ** [extendsFrom](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-extendsFrom"></a>
The name of the parent component type that this component type extends.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`

 ** [functions](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-functions"></a>
An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.
Type: String to [FunctionResponse](API_FunctionResponse.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`

 ** [isAbstract](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-isAbstract"></a>
A Boolean value that specifies whether the component type is abstract.
Type: Boolean

 ** [isSchemaInitialized](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-isSchemaInitialized"></a>
A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.
Type: Boolean

 ** [isSingleton](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-isSingleton"></a>
A Boolean value that specifies whether an entity can have more than one component of this type.
Type: Boolean

 ** [propertyDefinitions](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-propertyDefinitions"></a>
An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.
Type: String to [PropertyDefinitionResponse](API_PropertyDefinitionResponse.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`

 ** [propertyGroups](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-propertyGroups"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.
Type: String to [PropertyGroupResponse](API_PropertyGroupResponse.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`

 ** [status](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-status"></a>
The current status of the component type.
Type: [Status](API_Status.md) object

 ** [syncSource](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-syncSource"></a>
The syncSource of the SyncJob, if this entity was created by a SyncJob.
Type: String
Pattern: `[a-zA-Z_0-9]+`

 ** [updateDateTime](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-updateDateTime"></a>
The date and time when the component was last updated.
Type: Timestamp

 ** [workspaceId](#API_GetComponentType_ResponseSyntax) **   <a name="tm-GetComponentType-response-workspaceId"></a>
The ID of the workspace that contains the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

## Errors
<a name="API_GetComponentType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_GetComponentType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/GetComponentType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/GetComponentType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/GetComponentType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/GetComponentType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/GetComponentType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/GetComponentType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/GetComponentType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/GetComponentType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/GetComponentType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/GetComponentType)
