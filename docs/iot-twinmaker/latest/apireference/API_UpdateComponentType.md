---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdateComponentType.html
---

# UpdateComponentType
<a name="API_UpdateComponentType"></a>

Updates information in a component type.

## Request Syntax
<a name="API_UpdateComponentType_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}}/component-types/{{componentTypeId}} HTTP/1.1
Content-type: application/json

{
   "componentTypeName": "{{string}}",
   "compositeComponentTypes": {
      "{{string}}" : {
         "componentTypeId": "{{string}}"
      }
   },
   "description": "{{string}}",
   "extendsFrom": [ "{{string}}" ],
   "functions": {
      "{{string}}" : {
         "implementedBy": {
            "isNative": {{boolean}},
            "lambda": {
               "arn": "{{string}}"
            }
         },
         "requiredProperties": [ "{{string}}" ],
         "scope": "{{string}}"
      }
   },
   "isSingleton": {{boolean}},
   "propertyDefinitions": {
      "{{string}}" : {
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
      }
   },
   "propertyGroups": {
      "{{string}}" : {
         "groupType": "{{string}}",
         "propertyNames": [ "{{string}}" ]
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateComponentType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [componentTypeId](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-uri-componentTypeId"></a>
The ID of the component type.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: Yes

 ** [workspaceId](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-uri-workspaceId"></a>
The ID of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateComponentType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [componentTypeName](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-componentTypeName"></a>
The component type name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*[^\u0000-\u001F\u007F]*.*`
Required: No

 ** [compositeComponentTypes](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-compositeComponentTypes"></a>
This is an object that maps strings to `compositeComponentTypes` of the `componentType`. `CompositeComponentType` is referenced by `componentTypeId`.
Type: String to [CompositeComponentTypeRequest](API_CompositeComponentTypeRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** [description](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-description"></a>
The description of the component type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [extendsFrom](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-extendsFrom"></a>
Specifies the component type that this component type extends.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: No

 ** [functions](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-functions"></a>
An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.
Type: String to [FunctionRequest](API_FunctionRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** [isSingleton](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-isSingleton"></a>
A Boolean value that specifies whether an entity can have more than one component of this type.
Type: Boolean
Required: No

 ** [propertyDefinitions](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-propertyDefinitions"></a>
An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.
Type: String to [PropertyDefinitionRequest](API_PropertyDefinitionRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** [propertyGroups](#API_UpdateComponentType_RequestSyntax) **   <a name="tm-UpdateComponentType-request-propertyGroups"></a>
The property groups.
Type: String to [PropertyGroupRequest](API_PropertyGroupRequest.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Required: No

## Response Syntax
<a name="API_UpdateComponentType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "componentTypeId": "string",
   "state": "string",
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_UpdateComponentType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateComponentType_ResponseSyntax) **   <a name="tm-UpdateComponentType-response-arn"></a>
The ARN of the component type.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [componentTypeId](#API_UpdateComponentType_ResponseSyntax) **   <a name="tm-UpdateComponentType-response-componentTypeId"></a>
The ID of the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`

 ** [state](#API_UpdateComponentType_ResponseSyntax) **   <a name="tm-UpdateComponentType-response-state"></a>
The current state of the component type.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | ERROR`

 ** [workspaceId](#API_UpdateComponentType_ResponseSyntax) **   <a name="tm-UpdateComponentType-response-workspaceId"></a>
The ID of the workspace that contains the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

## Errors
<a name="API_UpdateComponentType_Errors"></a>

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
<a name="API_UpdateComponentType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/UpdateComponentType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/UpdateComponentType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/UpdateComponentType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/UpdateComponentType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/UpdateComponentType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/UpdateComponentType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/UpdateComponentType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/UpdateComponentType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/UpdateComponentType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/UpdateComponentType)
